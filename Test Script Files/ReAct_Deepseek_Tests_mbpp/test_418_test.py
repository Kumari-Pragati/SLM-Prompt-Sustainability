import unittest
from mbpp_418_code import Find_Max

class TestFindMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 5]), 5)

    def test_single_element(self):
        self.assertEqual(Find_Max([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(Find_Max([-1, -2, -3, -4, -5]), -1)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            Find_Max([])

    def test_duplicate_max(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 4]), 4)

    def test_large_numbers(self):
        self.assertEqual(Find_Max([1000000, 2000000, 3000000]), 3000000)
