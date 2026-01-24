import unittest
from mbpp_629_code import Split

class TestSplit(unittest.TestCase):

    def test_simple_even_numbers(self):
        self.assertListEqual(Split([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_mixed_even_and_odd_numbers(self):
        self.assertListEqual(Split([1, 2, 3, 4, 5, 6]), [2, 4])

    def test_empty_list(self):
        self.assertListEqual(Split([]), [])

    def test_single_even_number(self):
        self.assertListEqual(Split([2]), [2])

    def test_single_odd_number(self):
        self.assertListEqual(Split([1]), [])

    def test_min_max_values(self):
        self.assertListEqual(Split(range(2, 1000000, 2)), list(range(2, 1000000, 2)))

    def test_negative_numbers(self):
        self.assertListEqual(Split([-2, -4, -6]), [-2, -4])
