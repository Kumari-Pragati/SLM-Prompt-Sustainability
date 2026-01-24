import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_duplicate([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplicate([1]), [1])

    def test_duplicate_elements_list(self):
        self.assertEqual(remove_duplicate([1, 1, 2, 2, 3]), [1, 2, 3])

    def test_sorted_list(self):
        self.assertEqual(remove_duplicate([1, 2, 1, 3, 2]), [1, 2, 3])

    def test_unsorted_list(self):
        self.assertEqual(remove_duplicate([3, 2, 1, 2, 1]), [1, 2, 3])

    def test_list_with_duplicate_at_beginning_and_end(self):
        self.assertEqual(remove_duplicate([1, 1, 2, 2, 3, 1]), [1, 2, 3])

    def test_list_with_duplicate_in_middle(self):
        self.assertEqual(remove_duplicate([1, 2, 1, 2, 1, 3]), [1, 2, 3])

    def test_list_with_only_duplicates(self):
        self.assertEqual(remove_duplicate([1, 1]), [1])

    def test_list_with_negative_numbers(self):
        self.assertEqual(remove_duplicate([-1, -1, 0, 1]), [-1, 0, 1])

    def test_list_with_mixed_types(self):
        self.assertEqual(remove_duplicate([1, "a", 1]), [1, "a"])
