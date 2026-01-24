import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_duplicate([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplicate([1]), [1])

    def test_simple_list(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_list_with_duplicates_at_start_and_end(self):
        self.assertEqual(remove_duplicate([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1]), [2, 3, 4, 5])

    def test_list_with_duplicates_in_middle(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 3, 2, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_list_with_only_duplicates(self):
        self.assertEqual(remove_duplicate([1, 1, 1, 1]), [1])

    def test_list_with_only_different_elements(self):
        self.assertEqual(remove_duplicate([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_list_with_negative_numbers(self):
        self.assertEqual(remove_duplicate([-1, -2, -2, -3, -3, -4, -4, -5]), [-1, -2, -3, -4, -5])

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            remove_duplicate([1, "a", "a", 2])
