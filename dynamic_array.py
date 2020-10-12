# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME

import numpy as np

class DynamicArray:

    capacity = 10
    arrLength = 0
    arr = np.empty(0)
    data = np.arange(10, dtype=object)
    next_index = 0

    def __len__(self):
        return self.arrLength

    def __getitem__(self, item):
        return self.arr[item]

    def append(self, add):
        if self.arrLength == 0:
            self.arrLength += 1
            self.arr = np.array([add])
            self.data[0] = add
            self.next_index = 1

        else:
            new_arr = np.arange(self.arrLength*2, dtype=type(add))
            new_data = np.arange(self.arrLength*2, dtype=object)
            iter_arr = np.arange(self.arrLength)
            print(iter_arr[0])
            for x in iter_arr:
                new_arr[x] = self.arr[x]
                new_data[x] = self.arr[x]

            new_arr[self.arrLength] = new_data[self.arrLength] = add

            self.arr = new_arr
            self.data = new_data
            self.arrLength = (self.arrLength * 2)

            if(self.arrLength > 10):
                self.capacity = self.arrLength

    def is_empty(self):
        if self.arrLength == 0:
            return True


    pass
