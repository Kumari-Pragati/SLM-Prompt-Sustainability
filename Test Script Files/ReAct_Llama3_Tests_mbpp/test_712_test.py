import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_duplicate([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplicate([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4, 4, 5, 5, 5]), [1, 2, 3, 4, 5])

    def test_duplicates_at_start(self):
        self.assertEqual(remove_duplicate([2, 2, 2, 1]), [1, 2])

    def test_duplicates_in_middle(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_duplicates_at_end(self):
        self.assertEqual(remove_duplicate([1, 2, 3, 4, 4, 5, 5]), [1, 2, 3, 4, 5])

    def test_duplicates_everywhere(self):
        self.assertEqual(remove_duplicate([2, 2, 2, 1, 1, 3, 3, 3, 4, 4, 4, 5, 5, 5]), [1, 2, 3, 4, 5])

    def test_duplicates_and_non_duplicates(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7]), [1, 2, 3, 4, 5, 6, 7])
