import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(remove_even([]), [])

    def test_single_even_number(self):
        self.assertListEqual(remove_even([2]), [])

    def test_single_odd_number(self):
        self.assertListEqual(remove_even([1]), [1])

    def test_mixed_numbers(self):
        self.assertListEqual(remove_even([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_all_even_numbers(self):
        self.assertListEqual(remove_even([2, 4, 6]), [])

    def test_negative_numbers(self):
        self.assertListEqual(remove_even([-2, -4, -6]), [-1, -3])
