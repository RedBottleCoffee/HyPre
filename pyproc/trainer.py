from config import *
from models import Model
from util import *


alex = Model().build_alexnet()

path = 'samples/targets/00ad7068.wav'
data = load_wave(conf, path)
mel = sound_to_mels(conf, data)

print(mel)
print(type(mel))
print(mel.shape)
