import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_duplicate([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplicate([1]), [1])

    def test_duplicate_elements_list(self):
        self.assertEqual(remove_duplicate([1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_mixed_elements_list(self):
        self.assertEqual(remove_duplicate([1, 'a', 1, 'b', 2, 'a', 2, 'b']), [1, 'a', 2, 'b'])

    def test_negative_numbers_list(self):
        self.assertEqual(remove_duplicate([-1, -1, 0, 0, 1, 1]), [-1, 0, 1])

    def test_list_with_only_duplicates(self):
        self.assertEqual(remove_duplicate([1, 1, 1]), [1])

    def test_list_with_only_unique_elements(self):
        self.assertEqual(remove_duplicate([1, 2, 3]), [1, 2, 3])
