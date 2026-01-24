import unittest
from mbpp_831_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 2, 1]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 2)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_single_element_array(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_all_same_elements(self):
        arr = [4, 4, 4, 4, 4]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 6)

    def test_all_different_elements(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_large_array(self):
        arr = [i%3 for i in range(1000)]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 666666)
