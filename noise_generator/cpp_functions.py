import os
import ctypes

# test = ctypes.CDLL("D:\\cpp\\Dll1\\x64\\Debug\\Dll1.dll")
# test = ctypes.CDLL("C:\\Users\\smsha\\pyProjects\\TtH\\noise_generator\\Dll1.dll")

# dll_dir = r"C:\Users\smsha\pyProjects\TtH\noise_generator"
# dll = None
#
# try:
#     cookie = os.add_dll_directory(dll_dir)
#     dll_path = os.path.join(dll_dir, "Dll1.dll")
#     dll = ctypes.CDLL(dll_path)
# except OSError as error:
#     print("Failed to load Dll")
#     print(error)

dll_dir = r"C:\Users\smsha\pyProjects\TtH\noise_generator"

with os.add_dll_directory(dll_dir):
    # Use the full path here
    dll = ctypes.CDLL(os.path.join(dll_dir, "noise_generator.dll"), winmode=0)

dll.noise.restype = ctypes.c_double
dll.noise.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]


def noise(x: float, y: float, seed: int = 0, octaves: int = 1) -> float:
    return dll.noise(x, y, seed, octaves)


dll.distance_function.restype = ctypes.c_double
dll.distance_function.argtypes = [ctypes.c_double, ctypes.c_double]


def distance_function(x: float, y: float) -> float:
    return dll.distance_function(x, y)


dll.apply_distance_function.restype = ctypes.c_double
dll.apply_distance_function.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                         ctypes.c_int, ctypes.c_int, ctypes.c_int]


def apply_distance_function(_noise: float, _x: float, _y: float,
                            _width: int, _height: int, _magnification: int) -> float:
    return dll.apply_distance_function(_noise, _x, _y, _width, _height, _magnification)
