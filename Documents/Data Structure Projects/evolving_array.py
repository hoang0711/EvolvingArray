
# Implement a  Array ADT by writing the following methods: resize, append, insert_at_index,
#              remove_at_index, slice, merge, map, filter and reduce.


from static import StaticArray


class EvolvingArrayException(Exception):
    """
    Exception class for Array
    """
    pass


class EvolvingArray:
    def __init__(self, start_array=None):
        """
        Initialize new array
        """
        self._size = 0
        self._capacity = 6
        self._data = StaticArray(self._capacity)

        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return evolving array
        """
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        return out + ']'

    def __iter__(self):
        """
        Iterator for loop
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Return next value
        """
        try:
            value = self[self._index]
        except EvolvingArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index
        Raise EvolvingArrayException for invalid index
        """
        if index < 0 or index >= self._size:
            raise EvolvingArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index
        Raise EvolvingArrayException for invalid index
        """
        if index < 0 or index >= self._size:
            raise EvolvingArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True if array is empty
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return length of array
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return array's capacity
        """
        return self._capacity

    def print_array_data(self) -> None:
        """
        Print data within Evolving array
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")


    def resize(self, new_capacity: int) -> None:
        """
        Takes an integer as a new capacity and modifies the storage capacity of the array.
        """

        if new_capacity < 1 or new_capacity < self._size:
            return
        self._capacity = new_capacity

        # set up a new StaticArray with new capacity then copy the values from current array over to the new array
        new_array = StaticArray(new_capacity)
        for i in range(self._size):
            new_array[i] = self._data[i]

        # set current array's data equal to new array
        self._data = new_array


    def append(self, value: object) -> None:
        """
        Adds a new value at the end of the evolving array.
        """
        # if array's capacity is reached, call the resize method to double the capacity
        if self._size == self._capacity:
            self.resize(self._capacity * 2)

        # add the value to the current array and increment the size by 1
        self._data[self._size] = value
        self._size += 1

    def pop(self) -> None:
        """
        This method removes the last value from the end of the array.
        """
        # set the last element equal to None and decrement the array's size
        self._data[self._size - 1] = None
        self._size -= 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Takes 2 parameters and inserts that value at the provided index
        """
        # double the array's capacity if capacity and size are equal
        if index < 0 or index > self._size:
            raise EvolvingArrayException("Invalid index for insert method!")
        if self._size == self._capacity:
            self.resize(self._capacity * 2)

        # iterate backward from array's size to index and set the number at i equal to the previous number,
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """
        This method takes an index integer and removes the value at that provided index in the array.

        """
        # raise custom exception if index is negative or out of range
        if index < 0 or index > self._size - 1:
            raise EvolvingArrayException("Invalid index for remove method!")

        # if array's size is less than 1/4 of its capacity and twice of its size is equal or greater than 10
        # then resize the new capacity to twice the number of current elements
        if self._size < (self._capacity / 4) and self._size * 2 >= 10:
            self.resize(self._size * 2)

        # iterate from index to end of size, set element at i equal to next element, which will shift the
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1


    def slice(self, start_index: int, size: int) -> "EvolvingArray":
        """
        This method takes as parameters a start index and a size, and returns a new array with
        that size of elements at the requested index from the original array.
        """
        # if start index is negative or greater than the array's end then raise an exception
        if start_index < 0 or start_index > self._size - 1:
            raise EvolvingArrayException("Invalid start index for slice method!")
        if size < 0 or size > self._size - start_index:
            raise EvolvingArrayException("Invalid size for slice method!")

        # set up a new array and set up a last index of the slice
        # iterate through that slice from start to last index and add those elements to the new array

        for i in range(start_index, last_index):
            new_arr.append(self._data[i])

        # return the new array
        return new_arr

    def merge(self, second_da: "EvolvingArray") -> None:
        """
        This method takes a second  array and adds all of its elements onto the current array in
        the same order.
        """
        # iterate through the 2nd array's length and append all of its elements onto the current array
        for i in range(second_da.length()):
            self.append(second_da._data[i])

    def map(self, map_func) -> "EvolvingArray":
        """
        This method takes as parameter a map_function and returns a new array where each of its
        value is created by applying a given map_function.
        """
        # create a new array called mapped_arr
        mapped_arr = EvolvingArray()

        # iterate through the current array and append the new values derived by map_function to the new array
        for i in self:
            mapped_arr.append(map_func(i))

        # return the new array
        return mapped_arr

    def filter(self, filter_func) -> "EvolvingArray":
        """
        This method takes as parameter a filter_function and returns a new array which contains only
        elements that got tested and passed by the given filter_function (returns True).
        """
        # create a new array called filtered_arr
        filtered_arr = EvolvingArray()

        # iterate through the current array, if filter_function returns True for its values then append those
        # values to the new array
        for i in self:
            if filter_func(i):
                filtered_arr.append(i)

        # return the new array
        return filtered_arr

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        This method takes a reduce_function and an optional initializer as parameters. It will apply the
        reduce_function to all values within the current array and return the results.
        """
        # iterate through the current array, if the optional initializer is None then set it equal to the
        # value in the array. Otherwise, initializer will be equal to the resulting value of reduce_function
        for i in self:
            if initializer is None:
                initializer = i

        return initializer


def find_mode:
    """
    This method takes a array already in sorted order and returns a tuple containing a new
    array which contains the mode value and an integer that represents the highest frequency.
    """

    mode_arr = EvolvingArray()
    current_val = arr[0]
    current_freq = 1

    for i in range(1, arr.length()):
        if arr[i] == current_val:
            current_freq += 1

        else:
            current_val = arr[i]
            current_freq = 1

    for i in range(arr.length()):
        if arr[i] == max_val:
            mode_arr.append(arr[i])

    return (mode_arr, max_freq)

