import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):
    def test_find_tuples_empty_list(self):
        self.assertEqual(find_tuples([], 2), '[]')

    def test_find_tuples_single_element(self):
        self.assertEqual(find_tuples([4], 2), '["[4]"]')

    def test_find_tuples_multiple_elements(self):
        self.assertEqual(find_tuples([4, 8, 12, 16], 4), '["[4, 8, 12, 16]"]')

    def test_find_tuples_no_matching_elements(self):
        self.assertEqual(find_tuples([1, 3, 5], 2), '[]')

    def test_find_tuples_negative_numbers(self):
        self.assertEqual(find_tuples([-4, -8, -12, -16], 4), '["[-4, -8, -12, -16]"]')

    def test_find_tuples_mixed_numbers(self):
        self.assertEqual(find_tuples([4, -8, 12, -16, 0], 4), '["[4, -16]"]')

    def test_find_tuples_zero(self):
        self.assertEqual(find_tuples([0], 0), '["[0]"]')

    def test_find_tuples_non_integer_elements(self):
        self.assertEqual(find_tuples([4.0, 8, 12.0, 16], 4), '["[8, 12, 16]"]')
