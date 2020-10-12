# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME

import numpy as np
import traceback

class DynamicArray:

    capacity = 10
    arrLength = 0
    arr = np.empty(0)
    data = np.arange(10, dtype=object)
    next_index = 0

    def __len__(self):
        return self.arrLength

    def __getitem__(self, item):
        if(item > 0):
            traceback.format_exception_only(IndexError, item)
        else:
            return self.arr[item]

    def append(self, add):
        if self.arrLength == 0:
            self.arrLength += 1
            self.arr = np.array([add])
            self.data[0] = add
            self.next_index = 1

        else:
            new_len = self.arrLength+1
            new_arr = np.arange(new_len, dtype=object)
            new_data = np.arange(new_len, dtype=object)
            iter_arr = np.arange(self.arrLength)

            print('adding')
            for x in iter_arr:
                new_arr[x] = self.arr[x]
                new_data[x] = self.arr[x]
                print(new_data[x])

            new_arr[self.arrLength] = add
            new_data[self.arrLength] = add

            self.arr = new_arr
            self.data = new_data
            self.arrLength = new_len

            if(self.arrLength > 10):
                self.capacity = self.capacity*2

    def is_empty(self):
        if self.arrLength == 0:
            return True
    def clear(self):
        self.capacity = 10
        self.arrLength = 0
        self.arr = np.empty(0)
        self.data = np.arange(10, dtype=object)
        self.next_index = 0


    pass
