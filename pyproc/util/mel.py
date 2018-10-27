import numpy as np
import librosa
import wavio


def load_wave_first(path):
    w = wavio.read(fn_in)
    fs = w.rate
    bit = 8 * w.sampwidth
    data = w.data.T
    data = data / float( 2**(bit-1) )
    return data[0]

def load_wave_all(path):
    w = wavio.read(fn_in)
    fs = w.rate
    bit = 8 * w.sampwidth
    data = w.data.T
    data = data / float( 2**(bit-1) )
    return data

def sound_to_mels(conf, array):
    melspectrogram = librosa.feature.melspectrogram(array,
                                                 sr=conf.sampling_rate,
                                                 n_mels=conf.n_mels,
                                                 hop_length=conf.hop_length,
                                                 n_fft=conf.n_fft,
                                                 fmin=conf.fmin,
                                                 fmax=conf.fmax)
    melspectrogram = librosa.power_to_db(melspectrogram)
    melspectrogram = melspectrogram.astype(np.float32)

    return melspectrogram
