import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 0), "EVEN")
        self.assertEqual(check_last([1, 2, 3, 4], 4, 1), "ODD")

    def test_empty_list(self):
        self.assertEqual(check_last([], 0, 0), "Error: List is empty")

    def test_negative_number_in_list(self):
        self.assertEqual(check_last([-1, 2, 3, 4], 4, 0), "Error: Negative number in the list")

    def test_zero_in_list(self):
        self.assertEqual(check_last([0, 2, 3, 4], 4, 0), "EVEN")
        self.assertEqual(check_last([0, 2, 3, 4], 4, 1), "ODD")

    def test_negative_number_of_elements(self):
        self.assertEqual(check_last([1, 2, 3, 4], -1, 0), "Error: Invalid number of elements")
