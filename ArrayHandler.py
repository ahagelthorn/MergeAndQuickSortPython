class ArrayHandler():

    def __init__(self, array=[]):
        self.array = array

    def getArray(self):
        return self.array

    def getFirstValueInArray(self):
        return self.array[0]

    def getLastValueInArray(self):
        return self.array[-1]

    def quickSortPartition(self, start, end, array):

        pivot = array[start]
        i,j = start, end
        while i < j:
            while array[i] <= pivot:
                i += 1

            while array[j] > pivot:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]
        array[start], array[j] = array[j], array[start]
        return j


    def quickSort(self, start, end, array):

        if start < end:
            p = self.quickSortPartition(start, end, array)
            self.quickSort(start, p, array)
            self.quicksort(p + 1, end, array)

    def mergeSort(self, array):

        if len(array) > 1:
            m = len(array) // 2
            left = array[:m]
            right = array[m:]

            self.mergeSort(left)
            self.mergeSort(right)

            i,j,k = 0,0,0

            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1

