import unittest

from ArrayHandler import *

class Test(unittest.TestCase):

    def setUp(self):
        SAMPLE_ARRAY = [0, 1, 2, 3]
        testingArrayHandler = ArrayHandler(SAMPLE_ARRAY)
        return SAMPLE_ARRAY, testingArrayHandler

    def test_constructor_creates_correct_array(self):
        SAMPLE_ARRAY, testingArrayHandler = self.setUp()[0], self.setUp()[1]
        self.assertEqual(testingArrayHandler.getArray(), SAMPLE_ARRAY)

    def test_getFirstValueInArray_returns_correct_value(self):
        SAMPLE_ARRAY, testingArrayHandler = self.setUp()[0], self.setUp()[1]
        self.assertEqual(testingArrayHandler.getFirstValueInArray(), SAMPLE_ARRAY[0])

    def test_getLastValueInArray_returns_correct_value(self):
        SAMPLE_ARRAY, testingArrayHandler = self.setUp()[0], self.setUp()[1]
        self.assertEqual(testingArrayHandler.getLastValueInArray(), SAMPLE_ARRAY[-1])

    def test_quickSort_returns_sorted_list(self):
        sampleArray = [4, 0, 1, 2, 3]
        testingArrayHandler = ArrayHandler(sampleArray)
        self.assertEqual(testingArrayHandler.quickSort(testingArrayHandler.getFirstValueInArray(), testingArrayHandler.getLastValueInArray(), testingArrayHandler.getArray()), sampleArray.sort())

    def test_mergeSort_returns_sorted_list(self):
        sampleArray = [4, 0, 1, 2, 3]
        testingArrayHandler = ArrayHandler(sampleArray)
        self.assertEqual(testingArrayHandler.mergeSort(testingArrayHandler.getArray()), sampleArray.sort())