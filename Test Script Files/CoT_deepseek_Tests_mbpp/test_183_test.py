import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 7, 5, 9, 2, 12, 3, 2]
        n = len(arr)
        k = 2
        self.assertEqual(count_pairs(arr, n, k), 3)

    def test_reverse_order(self):
        arr = [12, 9, 7, 5, 3, 2, 1]
        n = len(arr)
        k = 2
        self.assertEqual(count_pairs(arr, n, k), 3)

    def test_single_element(self):
        arr = [5]
        n = len(arr)
        k = 2
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_no_pairs(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 6
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -2]
        n = len(arr)
        k = -1
        self.assertEqual(count_pairs(arr, n, k), 1)

    def test_large_numbers(self):
        arr = [10**6, 2*10**6, 3*10**6]
        n = len(arr)
        k = 10**6
        self.assertEqual(count_pairs(arr, n, k), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_pairs("not an array", 1, 1)
