class BinarySearch(list):
    def __init__(self, a, b):
        self.array = [i for i in range(b, a * b + 1, b)]
        self.length = len(self.array)
        super(BinarySearch, self).__init__(self.array)

    def search(self, param):
        count = 0
        array = self.array
        smaller = 0
        bigger = len(array)
        while smaller < bigger:
            count += 1
            middle = smaller + (bigger - smaller) // 2
            value = self.array[middle]
            if param == value:
                return {"count": count, "index": middle}
            elif param > value:
                if smaller == middle:
                    break
                smaller = middle
            else:
                bigger = middle - 1
        return {"count": count, "index": -1}
