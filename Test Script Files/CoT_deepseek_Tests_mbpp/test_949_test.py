import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_list([123, 45, 6789]), '[45, 123, 6789]')

    def test_single_digit_numbers(self):
        self.assertEqual(sort_list([1, 2, 3]), '[1, 2, 3]')

    def test_large_numbers(self):
        self.assertEqual(sort_list([123456789, 987654321]), '[987654321, 123456789]')

    def test_empty_list(self):
        self.assertEqual(sort_list([]), '[]')

    def test_negative_numbers(self):
        self.assertEqual(sort_list([-123, -45, -6789]), '[-6789, -123, -45]')

    def test_mixed_numbers(self):
        self.assertEqual(sort_list([123, -45, 6789]), '[-45, 123, 6789]')

    def test_duplicate_numbers(self):
        self.assertEqual(sort_list([123, 123, 6789]), '[123, 123, 6789]')
