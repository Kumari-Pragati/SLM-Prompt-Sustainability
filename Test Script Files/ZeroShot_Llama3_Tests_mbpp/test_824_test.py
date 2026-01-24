import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_remove_even_empty_list(self):
        self.assertEqual(remove_even([]), [])

    def test_remove_even_single_element(self):
        self.assertEqual(remove_even([1]), [1])

    def test_remove_even_multiple_elements(self):
        self.assertEqual(remove_even([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_remove_even_all_even(self):
        self.assertEqual(remove_even([2, 4, 6, 8]), [])

    def test_remove_even_mixed_list(self):
        self.assertEqual(remove_even([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 3, 5, 7, 9])

    def test_remove_even_list_with_duplicates(self):
        self.assertEqual(remove_even([2, 2, 4, 4, 6, 6]), [])
