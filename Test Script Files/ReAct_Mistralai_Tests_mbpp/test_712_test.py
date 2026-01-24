import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_duplicate([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplicate([1]), [1])

    def test_simple_list(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 5])

    def test_list_with_duplicates_at_beginning(self):
        self.assertEqual(remove_duplicate([2, 2, 1, 1, 3, 3]), [1, 2, 3])

    def test_list_with_duplicates_at_end(self):
        self.assertEqual(remove_duplicates([1, 1, 2, 2, 3]), [1, 2, 3])

    def test_list_with_duplicates_in_middle(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 2, 3, 3]), [1, 2, 3])

    def test_list_with_only_duplicates(self):
        self.assertEqual(remove_duplicates([2, 2]), [2])

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            remove_duplicates([1, "a", 2, "a"])

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            remove_duplicates([None, None, 1])
