import numpy as np

class BitVector:
    def __init__(self, size):
        self.__data = np.zeros((size // 64 + 1), dtype=np.uint)

    def set(self, index:int):
            byte_index = index // 64
            bit_index = index % 64
            self.__data[self.__data.shape[0] - byte_index - 1] |= np.uint(1 << bit_index)

    def reset(self, index:int):
        byte_index = index // 64
        bit_index = index % 64
        self.__data[self.__data.shape[0] - byte_index - 1] &= np.uint(~(1 << bit_index))


    def print(self):
        print(self.__data)

bv = BitVector(300)
bv.set(0)
bv.set(2)
bv.set(3)
bv.set(4)
bv.set(4)
bv.set(100)
bv.set(200)
bv.print()
