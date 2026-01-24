import unittest
from mbpp_932_code import remove_duplic_list

class TestRemoveDuplicList(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(remove_duplic_list([1, 2, 3, 2, 4, 1]), [1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(remove_duplic_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplic_list([1]), [1])

    def test_duplicate_list(self):
        self.assertEqual(remove_duplic_list([1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(remove_duplic_list([-1, -2, -3, -2, -4, -1]), [-1, -2, -3, -4])

    def test_mixed_numbers(self):
        self.assertEqual(remove_duplic_list([1, -2, 3, -4, 5]), [1, -2, 3, 5])

    def test_list_with_floats(self):
        self.assertEqual(remove_duplic_list([1.0, 2.0, 3.0, 2.0, 4.0, 1.0]), [1.0, 2.0, 3.0, 4.0])

    def test_list_with_strings(self):
        self.assertEqual(remove_duplic_list(["a", "b", "c", "b", "d"]), ["a", "b", "c", "d"])
