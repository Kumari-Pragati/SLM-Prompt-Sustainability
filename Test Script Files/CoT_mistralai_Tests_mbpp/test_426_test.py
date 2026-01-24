import unittest
from mbpp_426_code import filter_oddnumbers

class TestFilterOddNumbers(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], filter_oddnumbers([]))

    def test_single_even_number(self):
        self.assertListEqual([], filter_oddnumbers([2]))

    def test_single_odd_number(self):
        self.assertListEqual([4], filter_oddnumbers([4]))

    def test_multiple_odd_numbers(self):
        self.assertListEqual([1, 3, 5, 7], filter_oddnumbers([1, 2, 3, 4, 5, 6, 7]))

    def test_multiple_even_numbers(self):
        self.assertListEqual([], filter_oddnumbers([2, 4, 6]))

    def test_mixed_numbers(self):
        self.assertListEqual([1, 3, 5, 7, 9], filter_oddnumbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_negative_numbers(self):
        self.assertListEqual([-1, -3, -5, -7], filter_oddnumbers([-1, -2, -3, -4, -5, -6, -7]))

    def test_zero(self):
        self.assertListEqual([], filter_oddnumbers([0]))
