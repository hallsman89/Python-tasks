from time import time

import matrix
import mul_base

x = [[j for j in range(100)] for i in range(100)]
y = [[j for j in range(100)] for i in range(100)]


def show(matrix: list[list[int]]) -> None:
    for _ in matrix:
        print(_)
    print()


start_cy = time()
res_cy = matrix.mul(x, y)
end_cy = time()
time_cy = end_cy - start_cy

start_py = time()
res_py = mul_base.mul(x, y)
end_py = time()
time_py = end_py - start_py

assert res_cy == res_py

print(f"Cython time: {time_cy}")
print(f"Python time: {time_py}")
print(
    f"Difference between pure python and cython is {time_py - time_cy}"
    f"=> cython faster than python in {(time_py*10000)/(time_cy*10000)} times"
)
