import numpy as np
import librosa


def _load_wave(conf, path):
    data = librosa.load(path, sr=conf.sampling_rate)
    return np.asarray(data[0][:conf.samples * conf.duration])

def load_wavs(conf, paths):
    wavs = []
    for path in paths:
        wav = _load_wave(conf, path)
        wavs.append(wav)
    return wavs

def _sound_to_mel(conf, array):
    melspectrogram = librosa.feature.melspectrogram(array,
                                                 sr=conf.sampling_rate,
                                                 n_mels=conf.n_mels,
                                                 hop_length=conf.hop_length,
                                                 n_fft=conf.n_fft,
                                                 fmin=conf.fmin,
                                                 fmax=conf.fmax)
    melspectrogram = librosa.power_to_db(melspectrogram)
    melspectrogram = melspectrogram.astype(np.float32)

    return np.reshape(melspectrogram, (128, 128, 1))

def sounds_to_mels(conf, sound_array):
    mels = []
    for sound in sound_array:
        mel = _sound_to_mel(conf, sound)
        mel = np.reshape(mel, (128, 128, 1))
        mels.append(mel)
    return mels
