from model import make
import numpy as np
import sys
import os

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

Dp = 10
Hp = 175 
Wp = 175
T = 35

model = make(Dp, Hp, Wp, T)

model.summary()

model.compile('sgd', ['mse', 'mse'])


#Dp = 10
#Hp = 400
#Wp = 352
#T = 35


# TODO: data preparation, i.e. grouping and sampling (this is done outside the network)
x = np.random.random((1, Dp, Hp, Wp, T, 7))
y1 = np.random.random((1, Hp//2, Wp//2, 2))
y2 = np.random.random((1, Hp // 2, Wp // 2, 14))


def gen():
    yield x, [y1, y2]


# model.fit_generator(gen(), steps_per_epoch=1, epochs=1)

model.save('model/voxelnet' + '_D' + str(Dp) + '_H' + str(Hp) + '_W' + str(Wp) + '_T' + str(T) + '.h5')


