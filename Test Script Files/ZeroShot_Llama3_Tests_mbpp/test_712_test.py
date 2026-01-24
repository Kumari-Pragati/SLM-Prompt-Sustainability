import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_remove_duplicate(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4, 4, 5, 6, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(remove_duplicate([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_duplicate([]), [])
        self.assertEqual(remove_duplicate([1]), [1])
        self.assertEqual(remove_duplicate([1, 1, 1]), [1])
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]), [1, 2, 3, 4, 5])

    def test_remove_duplicate_empty_list(self):
        self.assertEqual(remove_duplicate([]), [])

    def test_remove_duplicate_single_element(self):
        self.assertEqual(remove_duplicate([1]), [1])

    def test_remove_duplicate_multiple_duplicates(self):
        self.assertEqual(remove_duplicate([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]), [1, 2, 3, 4, 5])

    def test_remove_duplicate_multiple_duplicates_and_order(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
