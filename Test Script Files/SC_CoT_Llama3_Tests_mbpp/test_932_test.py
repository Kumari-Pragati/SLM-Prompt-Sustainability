import unittest
from mbpp_932_code import remove_duplic_list

class TestRemoveDuplicList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_duplic_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplic_list([1]), [1])

    def test_duplicates(self):
        self.assertEqual(remove_duplic_list([1, 2, 2, 3, 4, 4]), [1, 2, 3, 4])

    def test_duplicates_order_matters(self):
        self.assertEqual(remove_duplic_list([4, 2, 2, 3, 1, 4]), [1, 2, 3, 4])

    def test_duplicates_order_matters_reverse(self):
        self.assertEqual(remove_duplic_list([4, 4, 3, 2, 2, 1]), [1, 2, 3, 4])

    def test_duplicates_order_matters_reverse_empty(self):
        self.assertEqual(remove_duplic_list([4, 4, 3, 2, 2, 1, 1]), [1, 2, 3, 4])

    def test_duplicates_order_matters_empty(self):
        self.assertEqual(remove_duplic_list([4, 4, 3, 2, 2, 1, 1, 1]), [1, 2, 3, 4])

    def test_duplicates_order_matters_empty_reverse(self):
        self.assertEqual(remove_duplic_list([4, 4, 3, 2, 2, 1, 1, 1, 1]), [1, 2, 3, 4])

    def test_duplicates_order_matters_empty_reverse_empty(self):
        self.assertEqual(remove_duplic_list([4, 4, 3, 2, 2, 1, 1, 1, 1, 1]), [1, 2, 3, 4])

    def test_duplicates_order_matters_empty_reverse_empty_reverse(self):
        self.assertEqual(remove_duplic_list([4, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1]), [1, 2, 3, 4])

    def test_duplicates_order_matters_empty_reverse_empty_reverse_empty(self):
        self.assertEqual(remove_duplic_list([4, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1]), [1, 2, 3, 4])

    def test_duplicates_order_matters_empty_reverse_empty_reverse_empty_reverse(self):
        self.assertEqual(remove_duplic_list([4, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]), [1, 2, 3, 4])

    def test_duplicates_order_matters_empty_reverse_empty_reverse_empty_reverse_empty(self):
        self.assertEqual(remove_duplic_list([4, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [1, 2, 3, 4])

    def test_duplicates_order_matters_empty_reverse_empty_reverse_empty_reverse_empty_reverse(self):
        self.assertEqual(remove_duplic_list([4, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [1, 2, 3, 4])

    def test_duplicates_order_matters_empty_reverse_empty_reverse_empty_reverse_empty_reverse_empty(self):
        self.assertEqual(remove_duplic_list([4, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [1, 2, 3, 4])

    def test_duplicates_order_matters_empty_reverse_empty_reverse_empty_reverse_empty_reverse_empty_reverse(self):
        self.assertEqual(remove_duplic_list([4, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [1, 2, 3, 4])

    def test_duplicates_order_matters_empty_reverse_empty_reverse_empty_reverse_empty_reverse_empty_reverse_empty(self):
        self.assertEqual(remove_duplic_list([4, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1,