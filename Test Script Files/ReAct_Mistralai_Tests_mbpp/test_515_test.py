import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):

    def test_empty_array(self):
        self.assertFalse(modular_sum([], 0, 1))

    def test_single_element(self):
        for n, m in [(0, 1), (1, 1), (0, 2), (1, 2), (0, 3), (1, 3)]:
            self.assertFalse(modular_sum([1], n, m))

    def test_positive_sum(self):
        for arr, n, m in [
            (([1, 2], 2, 3), True),
            (([1, 2], 3, 3), False),
            (([1, 2], 4, 3), True),
            (([1, 2], 5, 3), False),
            (([1, 2], 6, 3), True),
            (([1, 2], 7, 3), False),
            (([1, 2], 8, 3), True),
            (([1, 2], 9, 3), False),
            (([1, 2], 10, 3), True),
        ]:
            self.assertEqual(modular_sum(arr, n, m), arr[0] + arr[1] <= m)

    def test_negative_sum(self):
        for arr, n, m in [
            (([1, -2], 2, 3), False),
            (([1, -2], 3, 3), True),
            (([1, -2], 4, 3), False),
            (([1, -2], 5, 3), True),
            (([1, -2], 6, 3), False),
            (([1, -2], 7, 3), True),
            (([1, -2], 8, 3), False),
            (([1, -2], 9, 3), True),
            (([1, -2], 10, 3), False),
        ]:
            self.assertEqual(modular_sum(arr, n, m), arr[0] + arr[1] > m)

    def test_large_array(self):
        for n, m in [(1000, 1000), (1000, 1001), (1000, 999)]:
            arr = [i for i in range(1000)]
            self.assertEqual(modular_sum(arr, n, m), n > m)

    def test_negative_n(self):
        for arr, m in [([1, 2], 0), ([1, 2], -1)]:
            self.assertRaises(ValueError, modular_sum, arr, m, 3)

    def test_negative_m(self):
        for arr, n in [([1, 2], 3), ([1, 2], 4)]:
            self.assertRaises(ValueError, modular_sum, arr, n, -1)
