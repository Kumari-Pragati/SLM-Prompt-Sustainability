import unittest
from mbpp_418_code import Find_Max

class TestFindMax(unittest.TestCase):

    def test_find_max_positive_numbers(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 5]), 5)

    def test_find_max_negative_numbers(self):
        self.assertEqual(Find_Max([-1, -2, -3, -4, -5]), -1)

    def test_find_max_mixed_numbers(self):
        self.assertEqual(Find_Max([-1, 0, 1]), 1)

    def test_find_max_single_number(self):
        self.assertEqual(Find_Max([7]), 7)

    def test_find_max_empty_list(self):
        with self.assertRaises(ValueError):
            Find_Max([])
