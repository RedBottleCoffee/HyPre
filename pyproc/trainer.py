from modelable import Modelable

model = Modelable()
modelable = model        \
            .input()     \
            .conv2d()    \
            .normalize() \
            .conv2d()    \
