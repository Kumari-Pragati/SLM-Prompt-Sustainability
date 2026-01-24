import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):
    def test_remove_even_from_list(self):
        self.assertEqual(remove_even([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_remove_even_from_empty_list(self):
        self.assertEqual(remove_even([]), [])

    def test_remove_even_from_list_with_no_evens(self):
        self.assertEqual(remove_even([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_remove_even_from_list_with_all_evens(self):
        self.assertEqual(remove_even([2, 4, 6, 8, 10]), [])

    def test_remove_even_from_list_with_mixed_evens_and_odds(self):
        self.assertEqual(remove_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 3, 5, 7, 9])
