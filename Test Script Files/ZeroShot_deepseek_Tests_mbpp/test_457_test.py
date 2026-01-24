import unittest
from mbpp_457_code import Find_Min

class TestFindMin(unittest.TestCase):

    def test_find_min_with_positive_numbers(self):
        self.assertEqual(Find_Min([1, 2, 3, 4, 5]), 1)

    def test_find_min_with_negative_numbers(self):
        self.assertEqual(Find_Min([-1, -2, -3, -4, -5]), -5)

    def test_find_min_with_mixed_numbers(self):
        self.assertEqual(Find_Min([-1, 2, -3, 4, -5]), -5)

    def test_find_min_with_single_element(self):
        self.assertEqual(Find_Min([5]), 5)

    def test_find_min_with_empty_list(self):
        with self.assertRaises(ValueError):
            Find_Min([])
