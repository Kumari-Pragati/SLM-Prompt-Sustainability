import unittest
from mbpp_932_code import remove_duplic_list

class TestRemoveDuplicList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_duplic_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplic_list([1]), [1])

    def test_duplicates_in_list(self):
        self.assertEqual(remove_duplic_list([1, 2, 2, 3, 4, 4]), [1, 2, 3, 4])

    def test_no_duplicates_in_list(self):
        self.assertEqual(remove_duplic_list([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_list_with_duplicates_and_non_duplicates(self):
        self.assertEqual(remove_duplic_list([1, 2, 2, 3, 4, 5, 5, 6]), [1, 2, 3, 4, 5, 6])
