class BinarySearch(list):
    def __init__(self, a, b):
        self.array = [i for i in range(b, a * b, b)]
        self.length = len(self.array)

    def search(self, param):
        count = 0
        print(self.array)
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
                smaller = middle + 1
            else:
                bigger = middle - 1
        return {"count": count, "index": -1}
