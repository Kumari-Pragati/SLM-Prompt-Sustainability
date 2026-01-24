import unittest
from mbpp_296_code import get_Inv_Count

class TestGetInvCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_Inv_Count([], 0), 0)

    def test_single_element(self):
        for num in range(10):
            self.assertEqual(get_Inv_Count([num], num), 0)

    def test_increasing_sequence(self):
        for num in range(10):
            arr = list(range(num + 1))
            self.assertEqual(get_Inv_Count(arr, len(arr)), 0)

    def test_decreasing_sequence(self):
        for num in range(10):
            arr = list(range(num, 0, -1))
            self.assertEqual(get_Inv_Count(arr, len(arr)), num - 1)

    def test_mixed_sequence(self):
        arr = [5, 3, 8, 1, 6, 4, 9, 2, 7]
        self.assertEqual(get_Inv_Count(arr, len(arr)), 5)

    def test_duplicates(self):
        arr = [1, 1, 2, 3, 2, 2, 4, 3, 3]
        self.assertEqual(get_Inv_Count(arr, len(arr)), 4)

    def test_negative_numbers(self):
        arr = [-5, -3, -8, -1, -6, -4, -9, -2, -7]
        self.assertEqual(get_Inv_Count(arr, len(arr)), 15)

    def test_zero(self):
        self.assertEqual(get_Inv_Count([0], 1), 0)
        self.assertEqual(get_Inv_Count([0, 0], 2), 0)
        self.assertEqual(get_Inv_Count([0, 1, 0], 3), 1)

    def test_large_input(self):
        arr = [i for i in range(1000)]
        self.assertEqual(get_Inv_Count(arr, len(arr)), 499900)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            get_Inv_Count([1, 2, 3], -1)
        with self.assertRaises(ValueError):
            get_Inv_Count([], 10)
        with self.assertRaises(ValueError):
            get_Inv_Count([1, 2, 3], -10)
