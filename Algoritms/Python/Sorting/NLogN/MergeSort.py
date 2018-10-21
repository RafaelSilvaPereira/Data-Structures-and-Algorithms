class MergeSort:
        def merge(self,array, start, middle, end):
            # one array, but it's view as two arrays
            copy = array[::]

            indexA = start
            indexB = middle + 1

            indexK = start

            while indexA <= middle and indexB <= end:
                if copy[indexA] < copy[indexB]:
                    array[indexK] = copy[indexA]
                    indexA += 1
                else:
                    array[indexK] = copy[indexB]
                    indexB += 1

                indexK += 1

            while indexA <= middle:
                array[indexK] = copy[indexA]
                indexK += 1
                indexA += 1

            while indexB <= end:
                array[indexK] = copy[indexB]
                indexK += 1
                indexB += 1

        def Sort(self,array, start, end):

            if start < end:
                middle = (start + end) // 2
                self.Sort(array, start, middle)
                self.Sort(array, middle + 1, end)
                self.merge(array, start, middle, end)

        def Sort(self,array):
            self.Sort(array, 0, len(array) - 1)
