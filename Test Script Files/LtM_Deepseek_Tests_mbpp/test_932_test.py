import unittest
from mbpp_932_code import remove_duplic_list

class TestRemoveDuplicList(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(remove_duplic_list([1, 2, 2, 3, 4, 4]), [1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(remove_duplic_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplic_list([5]), [5])

    def test_duplicate_elements(self):
        self.assertEqual(remove_duplic_list([1, 1, 1, 1]), [1])

    def test_negative_numbers(self):
        self.assertEqual(remove_duplic_list([-1, -2, -2, -3]), [-1, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(remove_duplic_list([1, -1, 2, -2, 2, -2]), [1, -1, 2, -2])

    def test_large_numbers(self):
        self.assertEqual(remove_duplic_list(list(range(1, 10001))), list(range(1, 10001)))
