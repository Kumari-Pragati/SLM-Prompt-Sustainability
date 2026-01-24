import unittest
from mbpp_932_code import remove_duplic_list

class TestRemoveDuplicList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_duplic_list([1, 2, 2, 3, 4, 4]), [1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(remove_duplic_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplic_list([1]), [1])

    def test_all_duplicates_list(self):
        self.assertEqual(remove_duplic_list([1, 1, 1, 1]), [1])

    def test_negative_numbers(self):
        self.assertEqual(remove_duplic_list([-1, -2, -2, -3]), [-1, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(remove_duplic_list([1, -1, 2, -2, 2, -2]), [1, -1, 2, -2])

    def test_non_integer_numbers(self):
        self.assertEqual(remove_duplic_list([1.1, 2.2, 2.2, 3.3]), [1.1, 2.2, 3.3])

    def test_non_numeric_elements(self):
        self.assertEqual(remove_duplic_list(['a', 'b', 'b', 'c']), ['a', 'b', 'c'])

    def test_empty_string(self):
        self.assertEqual(remove_duplic_list(''), '')

    def test_string_with_duplicates(self):
        self.assertEqual(remove_duplic_list('aaabbb'), 'abc')
