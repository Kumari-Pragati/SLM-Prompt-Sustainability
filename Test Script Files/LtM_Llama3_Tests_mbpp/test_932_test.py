import unittest
from mbpp_932_code import remove_duplic_list

class TestRemoveDuplicList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_duplic_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplic_list([1]), [1])

    def test_duplicates_list(self):
        self.assertEqual(remove_duplic_list([1, 2, 2, 3, 1]), [1, 2, 3])

    def test_duplicates_list_with_order(self):
        self.assertEqual(remove_duplic_list([1, 2, 2, 3, 1, 4, 5, 5]), [1, 2, 3, 4, 5])

    def test_duplicates_list_with_order_and_duplicates(self):
        self.assertEqual(remove_duplic_list([1, 2, 2, 3, 1, 4, 5, 5, 6, 6]), [1, 2, 3, 4, 5, 6])

    def test_duplicates_list_with_order_and_duplicates_and_empty(self):
        self.assertEqual(remove_duplic_list([1, 2, 2, 3, 1, 4, 5, 5, 6, 6, []]), [1, 2, 3, 4, 5, 6])

    def test_duplicates_list_with_order_and_duplicates_and_empty_and_duplicates(self):
        self.assertEqual(remove_duplic_list([1, 2, 2, 3, 1, 4, 5, 5, 6, 6, [], 7, 7, 7]), [1, 2, 3, 4, 5, 6, 7])
