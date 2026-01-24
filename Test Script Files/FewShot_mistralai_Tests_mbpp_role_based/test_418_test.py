import unittest
from mbpp_418_code import Find_Max

class TestFindMax(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(Find_Max([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(Find_Max([1, -2, 3, -4, 5]), 5)

    def test_empty_list(self):
        self.assertIsNone(Find_Max([]))

    def test_single_element_list(self):
        self.assertEqual(Find_Max([1]), 1)

    def test_list_with_duplicates(self):
        self.assertEqual(Find_Max([1, 1, 2, 1, 3]), 3)

    def test_list_with_zero(self):
        self.assertEqual(Find_Max([0, 1, 2, 3]), 3)
