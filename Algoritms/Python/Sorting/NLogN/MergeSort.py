class MergeSort:
        def _merge(self, array, start, middle, end):
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

        def _sort(self, array, start, end):

            if start < end:
                middle = (start + end) // 2
                self._sort( array, start, middle )
                self._sort( array, middle + 1, end )
                self._merge( array, start, middle, end )

        def sort(self, array):
            self._sort( array, 0, len( array ) - 1 )
