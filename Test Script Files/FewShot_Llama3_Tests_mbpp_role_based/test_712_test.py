import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_duplicate([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplicate([1]), [1])

    def test_duplicates_in_list(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 1]), [1, 2, 3])

    def test_duplicates_in_list_with_order(self):
        self.assertEqual(remove_duplicate([4, 5, 5, 6, 4]), [4, 5, 6])

    def test_duplicates_in_list_with_order_and_duplicates(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 1, 4, 4, 5, 5]), [1, 2, 3, 4, 5])

    def test_list_with_duplicates_and_non_duplicates(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
