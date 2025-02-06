import ctypes
import numpy as np
from noise_generator.cpp_functions import noise, apply_distance_function


def generate_noise(width: int, height: int, map_size: int, shape: tuple, seed: int = 0) -> np.ndarray:
    noise_map: np.ndarray = np.zeros(width * height * 2, dtype=object)
    for y in range(-10, height):
        for x in range(width):
            num = '.'
            n = noise(x / 16.0, y / 16.0, seed, 8)
            n = apply_distance_function(n, x, y, width, height, 1) * 5.8
            if n > 0.1:
                num = '#'
            noise_map[y * width + x] = num

    return noise_map.reshape((1000, 1000)).transpose()


# a: np.ndarray = np.zeros(10 * 5)
# a = a.reshape((5, 10))
#
# for y in range(5):
#     for x in range(10):
#         print(a[y][x], end=" ")
#
#     print()

for i in range(-10, 20):
    print(i % 5, end=" ")
