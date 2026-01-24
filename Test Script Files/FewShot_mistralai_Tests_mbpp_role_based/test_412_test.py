import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(remove_odd([]), [])

    def test_single_even_number(self):
        self.assertListEqual(remove_odd([2]), [2])

    def test_single_odd_number(self):
        self.assertListEqual(remove_odd([1]), [])

    def test_mixed_list(self):
        self.assertListEqual(remove_odd([1, 2, 3, 4, 5]), [2, 4])

    def test_negative_numbers(self):
        self.assertListEqual(remove_odd([-2, -1, 0, 1, 2]), [-2, 0, 2])
