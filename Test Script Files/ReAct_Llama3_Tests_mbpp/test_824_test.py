import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_even([]), [])

    def test_list_with_no_even_numbers(self):
        self.assertEqual(remove_even([1, 3, 5, 7]), [1, 3, 5, 7])

    def test_list_with_one_even_number(self):
        self.assertEqual(remove_even([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_list_with_multiple_even_numbers(self):
        self.assertEqual(remove_even([2, 4, 6, 8, 10]), [])

    def test_list_with_mixed_numbers(self):
        self.assertEqual(remove_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 3, 5, 7, 9])

    def test_list_with_duplicates(self):
        self.assertEqual(remove_even([2, 2, 4, 4, 6, 6]), [])

    def test_list_with_negative_numbers(self):
        self.assertEqual(remove_even([-2, -4, -6, -8, -10]), [])
