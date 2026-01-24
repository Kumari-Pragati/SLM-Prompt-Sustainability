import unittest
from418_code import Find_Max

class TestFindMax(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(Find_Max([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(Find_Max([0, 0, 0]), 0)

    def test_edge_case_empty_list(self):
        self.assertIsNone(Find_Max([]))

    def test_edge_case_single_element(self):
        self.assertEqual(Find_Max([1]), 1)
        self.assertEqual(Find_Max([-1]), -1)
        self.assertEqual(Find_Max([0]), 0)

    def test_corner_case_negative_numbers_and_positive_numbers(self):
        self.assertEqual(Find_Max([-1, 1, -2, 2, -3, 3]), 3)
        self.assertEqual(Find_Max([-1, 1, -2, 2, -3, 3, 0]), 3)
