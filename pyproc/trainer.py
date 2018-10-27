from config import *
from models import Model
from util import *
from samples import *
from random import shuffle



alex = Model().build_alexnet()
alex.compile(optimizer='adam',
             loss='categorical_crossentropy',
             metrics=['accuracy'])

data = list(dataset.items())
shuffle(data)
wave_data, loaded_paths, loaded_labels = load_wavs(conf, data)
train_size = int(len(loaded_paths) * 0.8)

train_XX, test_XX = wave_data[:train_size], wave_data[train_size:]
train_X, test_X = sounds_to_mels(conf, train_XX), sounds_to_mels(conf, test_XX)
train_Y, test_Y = loaded_labels[:train_size], loaded_labels[train_size:]

alex.fit([train_X], [train_Y], epochs=500, batch_size=conf.batch_size, verbose=1, validation_data=([test_X], [test_Y]))
