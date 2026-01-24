import unittest
from mbpp_426_code import filter_oddnumbers

class TestFilterOddNumbers(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(filter_oddnumbers([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_empty_list(self):
        self.assertListEqual(filter_oddnumbers([]), [])

    def test_single_number(self):
        self.assertListEqual(filter_oddnumbers([1]), [1])

    def test_all_even(self):
        self.assertListEqual(filter_oddnumbers([2, 4, 6]), [])

    def test_boundary_case_zero(self):
        self.assertListEqual(filter_oddnumbers([0]), [])

    def test_negative_numbers(self):
        self.assertListEqual(filter_oddnumbers([-1, -3, -5]), [-1, -3])
