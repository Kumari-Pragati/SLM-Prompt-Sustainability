import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_duplicate([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplicate([1]), [1])

    def test_duplicates_in_list(self):
        self.assertEqual(remove_duplicate([1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_duplicates_in_list_with_order(self):
        self.assertEqual(remove_duplicate([3, 2, 1, 1, 2, 3]), [1, 2, 3])

    def test_duplicates_in_list_with_order_and_duplicates(self):
        self.assertEqual(remove_duplicate([3, 2, 1, 1, 2, 3, 3, 2, 1]), [1, 2, 3])

    def test_duplicates_in_list_with_order_and_duplicates_and_empty(self):
        self.assertEqual(remove_duplicate([3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3]), [1, 2, 3])

    def test_duplicates_in_list_with_order_and_duplicates_and_empty_and_duplicates(self):
        self.assertEqual(remove_duplicate([3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3]), [1, 2, 3])

    def test_duplicates_in_list_with_order_and_duplicates_and_empty_and_duplicates_and_duplicates(self):
        self.assertEqual(remove_duplicate([3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3]), [1, 2, 3])
