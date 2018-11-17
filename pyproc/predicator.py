import pyaudio
import sys
import array
import os
import numpy as np

from config import *
from util.mel import *
from time import sleep
from queue import Queue
from keras.models import load_model

audio = pyaudio.PyAudio()
history = Queue(maxsize=30)

def callback(in_data, frame_count, time_info, status):
    wav = array.array('h', in_data)
    history.put(wav, True)
    return(None, pyaudio.paContinue)

def gen_stream():
    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=44100,
        input=True,
        input_device_index=0,
        frames_per_buffer=2**11,
        start=False,
        stream_callback=callback
    )
    return stream

def restore_model():
    return load_model(os.path.dirname(os.path.abspath(__file__)) + '/model/alexnet.h5')

def parse_to_label(probs):
    result = np.argmax(probs)
    return conf.labels[result]

predicted = ['noise'] * 6
raw_audio_buffer = []
def main_process(model):
      global raw_audio_buffer
      while not history.empty():
          raw_audio_buffer.extend(history.get())
          if len(raw_audio_buffer) >= conf.mels_convert_samples: break
      if len(raw_audio_buffer) < conf.mels_convert_samples: return
      sound = np.array(raw_audio_buffer[:conf.sampling_rate * conf.duration]) / 32767
      raw_audio_buffer = raw_audio_buffer[conf.mels_onestep_samples:]
      melspectrogram = sound_to_mel(conf, sound)

      if melspectrogram is not None:
          reshaped = np.reshape(melspectrogram, (1, 128, 128, 1))
          probs = model.predict(reshaped)
          label = parse_to_label(probs)
          if not label in predicted and label is not 'noise':
              print(label, flush=True)
          predicted.append(label)
          predicted.pop(0)

if __name__ == '__main__':
    model = restore_model()
    stream = gen_stream()
    stream.start_stream()
    while stream.is_active():
        main_process(model)
        sleep(0.001)
    stream.stop_stream()
    stream.close()
    audio.terminate()
