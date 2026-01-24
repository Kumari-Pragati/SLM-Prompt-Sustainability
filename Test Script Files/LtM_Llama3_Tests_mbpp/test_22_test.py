import unittest
from mbpp_22_code import find_first_duplicate

class TestFindFirstDuplicate(unittest.TestCase):
    def test_no_duplicates(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 5]), -1)

    def test_single_duplicate(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 2, 4]), 2)

    def test_multiple_duplicates(self):
        self.assertEqual(find_first_duplicate([1, 2, 2, 3, 3, 3, 4]), 2)

    def test_duplicates_at_start(self):
        self.assertEqual(find_first_duplicate([2, 2, 3, 4, 5]), 2)

    def test_duplicates_at_end(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 5, 5]), 5)

    def test_duplicates_in_middle(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 2, 5]), 2)

    def test_empty_input(self):
        self.assertEqual(find_first_duplicate([]), -1)

    def test_single_element_input(self):
        self.assertEqual(find_first_duplicate([1]), -1)

    def test_duplicates_at_start_and_end(self):
        self.assertEqual(find_first_duplicate([2, 2, 3, 4, 5, 2]), 2)
