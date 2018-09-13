from numba import cuda
import numpy as np


@cuda.jit('void(int32[:], int32[:])')
def foo(arr_a, arr_b):
    tx = cuda.threadIdx.x
    bx = cuda.blockDim.x
    arr_b[bx * 5 + tx] = arr_a[bx * 5 + tx] + 1


arrA = np.arange(10)
devA = cuda.to_device(arrA)
arrB = np.zeros(10)
devB = cuda.to_device(arrB)
grid_dim = 2
block_dim = 5
foo[grid_dim, block_dim](arrA, arrB)
arrB = devB.copy_to_host()
