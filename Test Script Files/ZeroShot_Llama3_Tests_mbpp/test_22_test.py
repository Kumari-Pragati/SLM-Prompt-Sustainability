import unittest
from mbpp_22_code import find_first_duplicate

class TestFindFirstDuplicate(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_first_duplicate([]), -1)

    def test_single_element_list(self):
        self.assertEqual(find_first_duplicate([1]), -1)

    def test_no_duplicates(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 5]), -1)

    def test_one_duplicate(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 1]), 1)

    def test_multiple_duplicates(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 1, 2, 3]), 1)

    def test_duplicates_at_start(self):
        self.assertEqual(find_first_duplicate([1, 1, 2, 3, 4, 5]), 1)

    def test_duplicates_at_end(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 5, 1]), 1)

    def test_duplicates_in_middle(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 1, 4, 5]), 1)
