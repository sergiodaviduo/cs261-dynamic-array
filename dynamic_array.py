# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME

import numpy as np
import traceback

class DynamicArray:

    capacity = 10
    arrLength = 0
    data = np.arange(10, dtype=object)
    next_index = 0

    def __len__(self):
        return self.arrLength

    def __getitem__(self, item):
        try:
            out = self.data[item]
            if(self.arrLength == 0):
                a = np.arange(1)
                # I think this is cheating but......
                a[-100]
            return out
        except IndexError as e:
            raise IndexError('index out of range.')

    def append(self, add):
        len_ref = self.arrLength
        if (self.arrLength >= self.capacity):
            self.capacity = self.capacity * 2
            new_data = np.arange(self.capacity, dtype=object)

            for x in range(0,len_ref):
                new_data[x] = self.data[x]
            self.data = new_data

        if self.arrLength == 0:
            self.arrLength += 1
            self.data[0] = add
            self.next_index = 1
        else:
            self.data[self.arrLength] = add
            self.arrLength += 1
            self.next_index = self.arrLength

    def is_empty(self):
        if self.arrLength == 0:
            return True
    def clear(self):
        self.capacity = 10
        self.arrLength = 0
        self.data = np.arange(10, dtype=object)
        self.next_index = 0

    def pop(self):
        if (self.arrLength == 0):
            try:
                a = np.arange(1)
                # I think this is cheating but......
                a[-100]
            except IndexError as e:
                raise IndexError('index out of range.')

        to_pop = self.data[self.arrLength-1]
        new_data = np.arange(self.capacity, dtype=object)

        for x in range(0, self.arrLength-1):
            new_data[x] = self.data[x]

        self.data = new_data
        self.arrLength -= 1
        self.next_index = self.arrLength

        return to_pop

    def delete(self, index):
        if (self.arrLength == 0):
            try:
                a = np.arange(1)
                # I think this is cheating but......
                a[-100]
            except IndexError as e:
                raise IndexError('index out of range.')
        elif (index < 0 or index > self.arrLength-1):
            try:
                a = np.arange(1)
                # I think this is cheating but......
                a[-100]
            except IndexError as e:
                raise IndexError('index out of range.')

        new_data = np.arange(self.capacity, dtype=object)

        # for middle deletes, can use  var y, set as 0 initially, add to x, and when continue hits, set y to 1
        y = 0
        for x in range(0, self.arrLength - 1):
            if (index == x):
                y = 1
            new_data[x] = self.data[x+y]

        self.data = new_data
        self.arrLength -= 1
        self.next_index = self.arrLength

    def insert(self, index, item):
        if (self.arrLength == self.capacity):
            self.capacity = self.capacity * 2
        if (index < 0 or index > self.arrLength):
            try:
                a = np.arange(1)
                # I think this is cheating but......
                a[-100]
            except IndexError as e:
                raise IndexError('index out of range.')

        new_data = np.arange(self.capacity, dtype=object)

        y = 0
        z = 0
        # print('before')
        # for x in self.arr:
        #     print(str(x))
        # print("\n")
        for x in range(0, self.arrLength+1):
            # print('at '+str(x))
            if (index == x and index != 0):
                z = -1
                new_data[x] = item
            elif x == index == self.arrLength:
                new_data[x] = item
                break
            elif x == index == 0:
                new_data[x] = item
                z = -1
                continue
            else:
                new_data[x+y] = self.data[x+z]

            # print(str(new_arr[x]))
        self.data = new_data
        self.arrLength += 1
        self.next_index = self.arrLength

        # print('after')
        # for x in self.arr:
            # print(str(x))

    def is_full(self):
        if self.arrLength != self.capacity:
            return False
        else:
            return True

    def max(self):
        max = False

        for x in self.data:
            if max == False:
                max = x
            else:
                if x > max:
                    max = x

        if(self.is_empty() == True):
            return None
        return max

    def min(self):
        min = False

        for x in self.data:
            if min == False:
                min = x
            else:
                if x < min:
                    min = x

        if (self.is_empty() == True):
            return None
        return min

    def sum(self):
        sum = 0
        for x in self.data:
            sum += x

        if (self.is_empty() == True):
            return None
        return sum

    def linear_search(self, item):
        len_ref = self.arrLength
        arr_ref = self.data
        for x in range(0,len_ref):
            if(item == arr_ref[x]):
                return x
        return None

    # def binary_search(self, item):
    #     ordered = DynamicArray()
    #     backup = self.data
    #     result = False
    #
    #     for x in range(0,self.arrLength):
    #         ordered.insert(self.min())
    #         self.delete()
    #
    #     self.data = backup
    #
    #     return result
    # pass
