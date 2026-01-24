import unittest
from mbpp_932_code import remove_duplic_list

class TestRemoveDuplicList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_duplic_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplic_list([1]), [1])

    def test_list_with_duplicates(self):
        self.assertEqual(remove_duplic_list([1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_list_with_multiple_duplicates_and_unique_elements(self):
        self.assertEqual(remove_duplic_list([1, 1, 2, 2, 3, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_list_with_only_duplicates(self):
        self.assertEqual(remove_duplic_list([1, 1, 1]), [1])

    def test_list_with_only_negative_numbers(self):
        self.assertEqual(remove_duplic_list([-1, -1, -2, -2]), [-1, -2])

    def test_list_with_mixed_positive_and_negative_numbers(self):
        self.assertEqual(remove_duplic_list([1, 1, -2, -2, 3, 3]), [1, -2, 3])

    def test_list_with_only_floats(self):
        self.assertEqual(remove_duplic_list([1.1, 1.1, 2.2, 2.2]), [1.1, 2.2])

    def test_list_with_mixed_floats_and_integers(self):
        self.assertEqual(remove_duplic_list([1, 1.1, 2.2, 2, 2.2]), [1, 2.2])

    def test_list_with_strings(self):
        self.assertEqual(remove_duplic_list(['a', 'a', 'b', 'b']), ['a', 'b'])

    def test_list_with_mixed_strings_and_numbers(self):
        self.assertEqual(remove_duplic_list(['a', 1, 'a', 1]), ['a', 1])

    def test_list_with_lists(self):
        self.assertEqual(remove_duplic_list([[1], [1], [2], [2]]), [[1], [2]])

    def test_list_with_mixed_lists_and_numbers(self):
        self.assertEqual(remove_duplic_list([1, [1], 1, [1]]), [1, [1]])

    def test_list_with_lists_and_strings(self):
        self.assertEqual(remove_duplic_list([['a'], ['a'], [1], [1]]), [['a'], [1]])

    def test_list_with_lists_and_mixed_numbers_and_strings(self):
        self.assertEqual(remove_duplic_list([1, ['a'], 1, ['a']]), [1, ['a']])
