import ctypes

test = ctypes.CDLL("D:\\cpp\\Dll1\\x64\\Debug\\Dll1.dll")
# test = ctypes.CDLL("./Dll1.dll")

test.noise.restype = ctypes.c_double
test.noise.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]


def noise(x: float, y: float, seed: int = 0, octaves: int = 1) -> float:
    return test.noise(x, y, seed, octaves)


test.distance_function.restype = ctypes.c_double
test.distance_function.argtypes = [ctypes.c_double, ctypes.c_double]


def distance_function(x: float, y: float) -> float:
    return test.distance_function(x, y)


test.apply_distance_function.restype = ctypes.c_double
test.apply_distance_function.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                         ctypes.c_int, ctypes.c_int, ctypes.c_int]


def apply_distance_function(_noise: float, _x: float, _y: float,
                            _width: int, _height: int, _magnification: int) -> float:
    return test.apply_distance_function(_noise, _x, _y, _width, _height, _magnification)
