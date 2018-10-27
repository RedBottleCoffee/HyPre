from keras.layers import Input, Dense
from keras.models import Model
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPool2D, GlobalAveragePooling2D
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Adam
from keras.layers.core import Dense, Activation, Dropout, Flatten

class Modelable:
    def __init__(self, base=None):
        self.stream = base
        self.root = base

    def build(self):
        return Model(inputs=self.root, outputs=self.stream)

    def input(
        self,
        shape=(32, 32, 3)
    ):
        self.stream = Input(shape=shape)
        self.root = self.root or self.stream
        return self

    def conv2d(
        self,
        filters=32,
        kernel_size=(32, 32),
        strides=(1, 1),
        padding='same',
        activation='relu',
        use_bias=True,
        kernel_initializer='random_normal',
        bias_initializer='zeros'
    ):
        self.stream = Conv2D(
            filters=filters,
            kernel_size=kernel_size,
            strides=strides,
            padding=padding,
            activation=activation,
            use_bias=use_bias,
            kernel_initializer=kernel_initializer,
            bias_initializer=bias_initializer
          ) (self.stream)
        return self

    def mpool2d(
        self,
        pool_size=(2, 2),
        strides=(2, 2),
        padding='same'
    ):
        self.stream = MaxPool2D(
            pool_size=pool_size,
            strides=strides,
            padding=padding
          ) (self.stream)
        return self

    def gavgpool2d(
        self,
        data_format=None
    ):
        self.stream = GlobalAveragePooling2D(
            data_format=data_format
        ) (self.stream)
        return self

    def flat(
        self
    ):
        self.stream = Flatten() (self.stream)
        return self

    def fc(
        self,
        units=10,
        activation='relu',
        use_bias=True,
        kernel_initializer='glorot_uniform',
        bias_initializer='zeros'
    ):
        self.stream = Dence(
            units=units,
            activation=activation,
            use_bias=use_bias,
            kernel_initializer=kernel_initializer,
            bias_initializer=bias_initializer
        ) (self.stream)
        return self

    def normalize(
        self,
        axis=-1,
        momentum=0.99,
        epsilon=0.001,
        center=True,
        scale=True,
        beta_initializer='zeros',
        gamma_initializer='ones',
        moving_mean_initializer='zeros',
        moving_variance_initializer='ones',
        beta_regularizer=None,
        gamma_regularizer=None,
        beta_constraint=None,
        gamma_constraint=None
    ):
        self.stream = BatchNormalization(
            axis=-axis,
            momentum=momentum,
            epsilon=epsilon,
            center=center,
            scale=scale,
            beta_initializer=beta_initializer,
            gamma_initializer=gamma_initializer,
            moving_mean_initializer=moving_mean_initializer,
            moving_variance_initializer=moving_variance_initializer,
            beta_regularizer=beta_regularizer,
            gamma_regularizer=gamma_regularizer,
            beta_constraint=beta_constraint,
            gamma_constraint=gamma_constraint
        ) (self.stream)
        return self

    def dense(
        self,
        units,
        activation='relu',
        use_bias=True,
        kernel_initializer='glorot_uniform',
        bias_initializer='zeros',
        kernel_regularizer=None,
        bias_regularizer=None,
        activity_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None
     ):
        self.stream = Dense(
            units=units,
            activation=activation,
            use_bias=use_bias,
            kernel_initializer=kernel_initializer,
            bias_initializer=bias_initializer,
            kernel_regularizer=kernel_regularizer,
            bias_regularizer=bias_regularizer,
            activity_regularizer=activity_regularizer,
            kernel_constraint=kernel_constraint,
            bias_constraint=bias_constraint
        ) (self.stream)
        return self

    def dropout(
        self,
        rate=0.5,
        noise_shape=None,
        seed=None
    ):
        self.stream = Dropout(
            rate=rate,
            noise_shape=noise_shape,
            seed=seed
        ) (self.stream)
        return self
