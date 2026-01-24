import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(sum_Pairs(arr, n), 10)

    def test_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(sum_Pairs(arr, n), 0)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(sum_Pairs(arr, n), 0)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(sum_Pairs(arr, n), -10)

    def test_large_numbers(self):
        arr = [1000, 2000, 3000, 4000, 5000]
        n = len(arr)
        self.assertEqual(sum_Pairs(arr, n), 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_Pairs("not an array", 5)
