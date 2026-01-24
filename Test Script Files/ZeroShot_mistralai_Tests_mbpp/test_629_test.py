import unittest
from mbpp_629_code import Split

class TestSplitFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(Split([]), [])

    def test_single_even_number(self):
        self.assertListEqual(Split([2]), [2])

    def test_single_odd_number(self):
        self.assertListEqual(Split([1]), [])

    def test_mixed_numbers(self):
        self.assertListEqual(Split([1, 2, 3, 4, 5]), [2, 4])

    def test_all_even_numbers(self):
        self.assertListEqual(Split([2, 4, 6]), [2, 4, 6])

    def test_all_odd_numbers(self):
        self.assertListEqual(Split([1, 3, 5]), [])
