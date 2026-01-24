import unittest
from mbpp_554_code import Split

class TestSplit(unittest.TestCase):
    def test_simple_odd_numbers(self):
        self.assertListEqual(Split([1, 3, 5, 7]), [1, 3, 5, 7])

    def test_empty_list(self):
        self.assertListEqual(Split([]), [])

    def test_single_odd_number(self):
        self.assertListEqual(Split([1]), [1])

    def test_single_even_number(self):
        self.assertListEqual(Split([2]), [])

    def test_mixed_list(self):
        self.assertListEqual(Split([0, 1, 2, 3, 4, 5]), [1, 3])

    def test_min_max_values(self):
        self.assertListEqual(Split(range(1, 1000000, 2)), range(1, 1000000, 2))
