from keras.applications.mobilenetv2 import MobileNetV2

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

        return alexnet.build()



    def build_mobilenetv2(self):
        base = MobileNetV2(weights=None,
                           input_shape=conf.dims,
                           include_top=False,
                           alpha=0.35,
                           depth_multiplier=0.5)
        model = Modelable(base.output)
        mobilenetv2 = model \
                      .gavgpool2d() \
                      .dense(1024) \
                      .dense(conf.num_classes, activation='softmax')

        return mobilenetv2.build()
