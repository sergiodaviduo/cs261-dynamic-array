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
        if(item > self.arrLength):
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

    def pop(self):
        if(self.arrLength == 0):
            traceback.format_exception_only(IndexError, self.arrLength)

        to_pop = self.arr[self.arrLength-1]
        new_arr = np.arange(self.arrLength, dtype=object)

        for x in range(0, self.arrLength-1):
            new_arr[x] = self.arr[x]

        self.arr = new_arr

        self.arrLength -= 1

        return to_pop

    def delete(self, index):
        if (self.arrLength == 0):
            traceback.format_exception_only(IndexError, self.arrLength)
        elif (index < 0 or index > self.arrLength-1):
            try:
                # I think this is cheating but......
                a = [1]
                b = a[2]
            except IndexError as e:
                raise IndexError('index out of range.')

        new_arr = np.arange(self.arrLength, dtype=object)
        # for middle deletes, can use  var y, set as 0 initially, add to x, and when continue hits, set y to 1
        y = 0
        for x in range(0, self.arrLength - 1):
            if (index == x):
                y = 1
            new_arr[x] = self.arr[x+y]

        self.arr = new_arr

        self.arrLength -= 1
    pass
