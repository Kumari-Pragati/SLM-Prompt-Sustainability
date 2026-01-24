import unittest
from mbpp_22_code import find_first_duplicate

class TestFindFirstDuplicate(unittest.TestCase):

    def test_with_duplicates(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 2]), 2)
        self.assertEqual(find_first_duplicate([1, 2, 3, 1]), 1)
        self.assertEqual(find_first_duplicate([1, 2, 2, 3]), 2)

    def test_no_duplicates(self):
        self.assertEqual(find_first_duplicate([1, 2, 3]), -1)
        self.assertEqual(find_first_duplicate([1, 2, 3, 4]), -1)

    def test_empty_list(self):
        self.assertEqual(find_first_duplicate([]), -1)

    def test_single_element(self):
        self.assertEqual(find_first_duplicate([1]), -1)
