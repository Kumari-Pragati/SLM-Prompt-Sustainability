import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):

    def test_simple_subtract(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

    def test_empty_lists(self):
        self.assertEqual(sub_list([], []), [])

    def test_negative_numbers(self):
        self.assertEqual(sub_list([-1, -2, -3], [-4, -5, -6]), [3, 3, 3])

    def test_mixed_numbers(self):
        self.assertEqual(sub_list([1, -2, 3], [-4, 5, -6]), [5, -7, 9])

    def test_large_numbers(self):
        self.assertEqual(sub_list([1000000, 2000000, 3000000], [100000, 200000, 300000]), [900000, 1800000, 2700000])

    def test_unequal_lengths(self):
        self.assertEqual(sub_list([1, 2, 3, 4], [1, 2]), [0, 0])
