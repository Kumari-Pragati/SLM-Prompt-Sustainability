import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(find_minimum_range([]))

    def test_single_element_list(self):
        self.assertEqual(find_minimum_range([[1]]), (1, 1))

    def test_two_element_list(self):
        self.assertEqual(find_minimum_range([[1, 2]]), (1, 2))

    def test_three_element_list(self):
        self.assertEqual(find_minimum_range([[1, 2, 3]]), (1, 3))

    def test_list_with_duplicates(self):
        self.assertEqual(find_minimum_range([[1, 1, 2, 2, 3, 3]]), (1, 3))

    def test_list_with_negative_numbers(self):
        self.assertEqual(find_minimum_range([[-1, -2, -3]]), (-3, -1))

    def test_list_with_positive_and_negative_numbers(self):
        self.assertEqual(find_minimum_range([[1, -2, 3, -4]]), (-4, 3))

    def test_list_with_repeated_ranges(self):
        self.assertEqual(find_minimum_range([[1, 2, 3, 2, 1]]), (1, 3))

    def test_list_with_empty_sublist(self):
        self.assertEqual(find_minimum_range([[1, 2, [], 4]]), (1, 4))

    def test_list_with_sublist_of_length_one(self):
        self.assertEqual(find_minimum_range([[1, 2, [3], 4]]), (1, 4))

    def test_list_with_sublist_of_length_zero(self):
        self.assertEqual(find_minimum_range([[1, 2, [], 4]]), (1, 4))
