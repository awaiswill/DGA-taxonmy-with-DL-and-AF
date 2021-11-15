from keras import backend as K


def swish(x):
    beta = 1
    return K.sigmoid(x * beta) * x


def penalized_tanh(x):
    alpha = 0.25
    return K.maximum(tanh(x), alpha*tanh(x))


def tanh(x):
    return K.tanh(x)


def z_function(x):
    alpha = 0.5
    return (alpha * x) + (exponential(-1 * K.pow(x, 2)))


def new_function(x):
    return math.pi * x * (exponential(-1 * K.pow(x, 2)))


def alpha_function(x):
    return x/(x + exponential(-1 * x))


def exponential(x):
    return K.exp(x)
