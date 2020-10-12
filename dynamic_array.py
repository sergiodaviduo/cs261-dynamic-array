# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME

import numpy as np

class DynamicArray:

    capacity = 10
    arrLength = 0
    arr = np.empty(0)

    def __len__(self):
        return self.arrLength

    def __getitem__(self, item):
        return self.arr[item]

    def append(self, add):
        if self.arrLength == 0:
            self.arrLength += 1
            self.arr =np.array([add])
        else:
            self.arrLength = (self.arrLength*2)
            new_arr = np.arange(self.arrLength)
            for x in new_arr:
                self.arr[x] = x     # only works because of numpy defaults

    def is_empty(self):
        if self.arrLength == 0:
            return True

    pass
