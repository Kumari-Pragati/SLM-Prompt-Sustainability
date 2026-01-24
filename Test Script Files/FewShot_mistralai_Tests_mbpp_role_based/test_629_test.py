import unittest
from mbpp_629_code import Split

class TestSplit(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(Split([]), [])

    def test_single_even_number(self):
        self.assertListEqual(Split([2]), [2])

    def test_single_odd_number(self):
        self.assertListEqual(Split([1]), [])

    def test_mixed_list(self):
        self.assertListEqual(Split([1, 2, 3, 4, 5]), [2, 4])

    def test_negative_numbers(self):
        self.assertListEqual(Split([-2, -4, -6]), [-2, -4])

    def test_large_numbers(self):
        self.assertListEqual(Split([10000, 10002, 10004]), [10000, 10004])
