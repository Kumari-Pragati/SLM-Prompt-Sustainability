import unittest
from mbpp_867_code import min_Num

class TestMinNum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(min_Num([], 0), 2)

    def test_single_odd_element(self):
        self.assertEqual(min_Num([1], 1), 1)
        self.assertEqual(min_Num([3], 1), 1)
        self.assertEqual(min_Num([5], 1), 1)

    def test_single_even_element(self):
        self.assertEqual(min_Num([2], 1), 2)
        self.assertEqual(min_Num([4], 1), 2)
        self.assertEqual(min_Num([6], 1), 2)

    def test_mixed_list(self):
        self.assertEqual(min_Num([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(min_Num([2, 1, 0, 3, 4], 5), 2)
        self.assertEqual(min_Num([3, 5, 1, 2, 4], 5), 1)

    def test_boundary_cases(self):
        self.assertEqual(min_Num([0], 1), 2)
        self.assertEqual(min_Num([1], 0), 1)
        self.assertEqual(min_Num([-1], 1), 1)
        self.assertEqual(min_Num([1], -1), 1)

    def test_large_list(self):
        arr = [i for i in range(100)]
        self.assertEqual(min_Num(arr, len(arr)), 1 if sum(1 for i in arr if i % 2) % 2 else 2)
