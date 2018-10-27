from config import *
from models import Model
from util import *
from samples import *
from random import shuffle



alex = Model().build_alexnet()

data = list(dataset.items())
shuffle(data)
train_size = int(len(data) * 0.8)
train, test = data[:train_size], data[train_size:]

alex.compile(optimizer='adam',
             loss='categorical_crossentropy',
             metrics=['accuracy'])

data_paths = dict(train).keys()
wave_data = load_wavs(conf, data_paths)
train_X = sounds_to_mels(conf, wave_data)
train_Y = list(dict(train).values())

# train_Y =

alex.fit([train_X], [train_Y], epochs=500, batch_size=conf.batch_size, verbose=1)
