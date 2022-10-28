class ArrayPairSum:
    """
    PROBLEM: Given an integer array, output all the unique pairs that sum up to a specific value k.
    So the input:
        pair_sum([1, 3, 2, 2], 4)
    would return 2 pairs:
        (1, 3)
        (2, 2)
    """

    def __init__(self, arr, k):
        self.array = arr
        self.sum = k

    def pair_sum(self):
        lst = []
        count = 0
        for x in range(0, len(self.array)):
            for y in range(x+1, len(self.array)):
                if self.array[x] + self.array[y] == self.sum:
                    count += 1
                    lst.append((self.array[x], self.array[y]))
        return count, lst


if __name__ == '__main__':
    p_sum = ArrayPairSum([1, 2, 3, 1], 3)
    print(p_sum.pair_sum())
