import unittest
from mbpp_932_code import remove_duplic_list

class TestRemoveDuplicList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_duplic_list([1, 2, 3, 2, 4, 1]), [1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(remove_duplic_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplic_list([1]), [1])

    def test_duplicate_at_beginning(self):
        self.assertEqual(remove_duplic_list([2, 2, 3, 4]), [3, 4])

    def test_duplicate_at_end(self):
        self.assertEqual(remove_duplic_list([1, 2, 2]), [1, 2])

    def test_duplicate_in_middle(self):
        self.assertEqual(remove_duplic_list([1, 2, 2, 3]), [1, 2, 3])

    def test_duplicate_only_case(self):
        self.assertEqual(remove_duplic_list([2, 2]), [2])

    def test_negative_numbers(self):
        self.assertEqual(remove_duplic_list([-1, -2, -3, -2, -4, -1]), [-1, -2, -3, -4])

    def test_mixed_numbers(self):
        self.assertEqual(remove_duplic_list([1, -2, 3, -4, 2]), [1, -2, 3])
