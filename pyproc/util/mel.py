import numpy as np
import librosa


def load_wave(conf, path):
    data = librosa.load(path, sr=conf.sampling_rate)
    return np.asarray(data[0][:conf.samples * conf.duration])

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
