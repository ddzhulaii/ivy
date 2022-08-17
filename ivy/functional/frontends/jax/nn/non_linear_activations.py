import ivy


def relu(x):
    return ivy.relu(x)


relu.unsupported_dtypes = {"torch": ("float16", "bfloat16")}


def leaky_relu(x, negative_slope=0.01):
    return ivy.leaky_relu(x, alpha=negative_slope)


leaky_relu.unsupported_dtypes = {"torch": ("float16", "bfloat16")}


def gelu(x, approximate=True):
    return ivy.gelu(x, approximate=approximate)


gelu.unsupported_dtypes = {"torch": ("float16", "bfloat16")}


def sigmoid(x):
    return ivy.sigmoid(x)


sigmoid.unsupported_dtypes = {"torch": ("float16", "bfloat16")}


def one_hot(x, num_classes, *, device=None, out=None):
    return ivy.one_hot(x, num_classes, device=device, out=out)


def softmax(x, /, *, axis=None):
    return ivy.softmax(x, axis=axis)


def softplus(x):
    return ivy.softplus(x)