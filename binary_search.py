class BinarySearch(list):
    def __init__(self, a, b):
        self.array = [i for i in range(b, a * b + 1, b)]
        self.length = len(self.array)
        super(BinarySearch, self).__init__(self.array)

    def search(self, value_to_search):
        count = 0
        array = self.array
        smaller = 0
        bigger = len(array)

        if value_to_search == array[-1] : return {"count": count, "index": bigger - 1}
        if value_to_search == array[0]: return {"count": count, "index": smaller}

        while smaller < bigger:
            middle = smaller + (bigger - smaller) // 2
            value = self.array[middle]
            if value_to_search == value:
                return {"count": count, "index": middle}
            elif value_to_search > value:
                if smaller == middle:
                    break
                smaller = middle
            else:
                bigger = middle - 1
            count += 1
        return {"count": count-1, "index": -1}