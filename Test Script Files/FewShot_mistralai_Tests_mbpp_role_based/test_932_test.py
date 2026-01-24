import unittest
from mbpp_932_code import remove_duplic_list

class TestRemoveDuplicList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_duplic_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplic_list([1]), [1])

    def test_duplicates_in_list(self):
        self.assertEqual(remove_duplic_list([1, 1, 2, 2, 3]), [1, 2, 3])

    def test_list_with_duplicates_at_beginning(self):
        self.assertEqual(remove_duplic_list([1, 1, 2]), [2, 1])

    def test_list_with_duplicates_at_end(self):
        self.assertEqual(remove_duplic_list([1, 2, 2]), [1, 2])

    def test_list_with_duplicates_in_middle(self):
        self.assertEqual(remove_duplic_list([1, 2, 1, 2]), [1, 2])

    def test_list_with_only_duplicates(self):
        self.assertEqual(remove_duplic_list([1, 1]), [])

    def test_list_with_non_numeric_elements(self):
        self.assertEqual(remove_duplic_list(['a', 'b', 'a']), ['a', 'b'])
