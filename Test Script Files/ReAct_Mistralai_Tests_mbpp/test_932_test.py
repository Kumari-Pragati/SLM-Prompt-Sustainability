import unittest
from mbpp_932_code import remove_duplic_list

class TestRemoveDuplicList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_duplic_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplic_list([1]), [1])

    def test_list_with_duplicates(self):
        self.assertEqual(remove_duplic_list([1, 1, 2, 2, 3]), [1, 2, 3])

    def test_list_with_only_duplicates(self):
        self.assertEqual(remove_duplic_list([1, 1]), [1])

    def test_list_with_mixed_duplicates_and_unique_elements(self):
        self.assertEqual(remove_duplic_list([1, 2, 1, 3, 2]), [1, 2, 3])

    def test_list_with_negative_numbers(self):
        self.assertEqual(remove_duplic_list([1, -1, 1]), [1, -1])

    def test_list_with_floats(self):
        self.assertEqual(remove_duplic_list([1.0, 1.0, 2.0]), [1.0, 2.0])

    def test_list_with_strings(self):
        self.assertEqual(remove_duplic_list(['a', 'a', 'b']), ['a', 'b'])

    def test_list_with_lists(self):
        self.assertEqual(remove_duplic_list([[1], [1], [2]]), [[1], [2]])

    def test_list_with_mixed_types(self):
        self.assertEqual(remove_duplic_list([1, 'a', 1]), [1, 'a'])

    def test_list_with_large_numbers(self):
        self.assertEqual(remove_duplic_list(list(range(1000000))), list(range(1000000)))
