import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 6)

    def test_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_duplicate_elements(self):
        arr = [1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 3)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 10)

    def test_mixed_numbers(self):
        arr = [-1, 2, -3, 4, -5]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 9)
