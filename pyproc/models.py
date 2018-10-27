from modelable import Modelable
from config import *

class Model:
    def __init__(self):
        pass

    def build_alexnet(self):
        model = Modelable()
        alexnet = model        \
                  .input(conf.dims)     \
                  .conv2d(48, 11, strides=(2, 3)) \
                  .mpool2d(3, strides=(1, 2)) \
                  .normalize() \
                  .conv2d(128, 5, strides=(2, 3)) \
                  .mpool2d(3, strides=2) \
                  .normalize() \
                  .conv2d(192, 3, strides=(1, 2))    \
                  .conv2d(192, 3, strides=(1, 1)) \
                  .conv2d(128, 3, strides=(1, 1)) \
                  .mpool2d(3, strides=(1, 2)) \
                  .normalize() \
                  .flat() \
                  .dense(256) \
                  .dropout(0.5) \
                  .dense(256) \
                  .dropout(0.5) \
                  .dense(conf.num_classes, activation='softmax')
        return alexnet



    def build_mobilenetv2(self):
        model = Modelable()
        # modelable = model
