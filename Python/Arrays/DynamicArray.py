import ctypes


class DynamicArray(object):

    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.array_1 = self.make_array(self.capacity)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if not 0 <= index < self.length:
            return IndexError('Index is out of bounds!')

        return self.array_1[index]

    def append(self, element):
        if self.length == self.capacity:
            self._resize(2 * self.capacity)

        self.array_1[self.length] = element
        self.length += 1

    def _resize(self, new_capacity):
        array_2 = self.make_array(new_capacity)

        for i in range(self.length):
            array_2[i] = self.array_1[i]

        self.array_1 = array_2
        self.capacity = new_capacity

    @staticmethod
    def make_array(new_capacity):
        return (new_capacity * ctypes.py_object)()


if __name__ == '__main__':
    array = DynamicArray()
    array.append(1)
    print(len(array))
    array.append(2)
    print(len(array))
    print(array[1])
    print(array[5])
