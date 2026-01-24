import unittest

from mbpp_932_code import remove_duplic_list

class TestRemoveDuplicList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_duplic_list([1, 2, 2, 3, 4, 4]), [1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(remove_duplic_list([]), [])

    def test_single_element(self):
        self.assertEqual(remove_duplic_list([1]), [1])

    def test_all_duplicates(self):
        self.assertEqual(remove_duplic_list([1, 1, 1, 1]), [1])

    def test_negative_numbers(self):
        self.assertEqual(remove_duplic_list([-1, -2, -2, -3]), [-1, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(remove_duplic_list([1, 2, -1, -2]), [1, 2, -1, -2])

    def test_duplicate_strings(self):
        self.assertEqual(remove_duplic_list(['a', 'b', 'b', 'c']), ['a', 'b', 'c'])

    def test_empty_strings(self):
        self.assertEqual(remove_duplic_list(['', '']), [''])

    def test_single_string(self):
        self.assertEqual(remove_duplic_list(['a']), ['a'])

    def test_all_duplicates_strings(self):
        self.assertEqual(remove_duplic_list(['a', 'a', 'a', 'a']), ['a'])

    def test_mixed_strings(self):
        self.assertEqual(remove_duplic_list(['a', 'b', '', '']), ['a', 'b', '', ''])
