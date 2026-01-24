import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):

    def test_typical_case(self):
        a = [1, 2, 3, 4]
        n = len(a)
        k = 2
        self.assertEqual(max_sub_array_sum_repeated(a, n, k), 10)

    def test_negative_numbers(self):
        a = [-1, -2, -3, -4]
        n = len(a)
        k = 2
        self.assertEqual(max_sub_array_sum_repeated(a, n, k), -1)

    def test_single_element(self):
        a = [5]
        n = len(a)
        k = 2
        self.assertEqual(max_sub_array_sum_repeated(a, n, k), 5)

    def test_empty_array(self):
        a = []
        n = len(a)
        k = 2
        self.assertEqual(max_sub_array_sum_repeated(a, n, k), 0)

    def test_large_numbers(self):
        a = [1000, 2000, 3000, 4000]
        n = len(a)
        k = 2
        self.assertEqual(max_sub_array_sum_repeated(a, n, k), 10000)

    def test_large_k(self):
        a = [1, 2, 3, 4]
        n = len(a)
        k = 10
        self.assertEqual(max_sub_array_sum_repeated(a, n, k), 10)

    def test_negative_k(self):
        a = [1, 2, 3, 4]
        n = len(a)
        k = -1
        with self.assertRaises(ValueError):
            max_sub_array_sum_repeated(a, n, k)

    def test_zero_k(self):
        a = [1, 2, 3, 4]
        n = len(a)
        k = 0
        with self.assertRaises(ValueError):
            max_sub_array_sum_repeated(a, n, k)
