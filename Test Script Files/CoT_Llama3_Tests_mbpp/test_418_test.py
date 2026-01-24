import unittest
from mbpp_418_code import Find_Max

class TestFind_Max(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 5]), 5)

    def test_edge_case(self):
        self.assertEqual(Find_Max([-1, -2, -3, -4, -5]), -5)

    def test_edge_case2(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 5, 6]), 6)

    def test_edge_case3(self):
        self.assertEqual(Find_Max([-1, -2, -3, -4, -5, -6]), -6)

    def test_empty_list(self):
        self.assertRaises(ValueError, Find_Max, [])

    def test_single_element_list(self):
        self.assertEqual(Find_Max([1]), 1)

    def test_list_with_duplicates(self):
        self.assertEqual(Find_Max([1, 2, 2, 3, 4, 5]), 5)

    def test_list_with_negative_numbers(self):
        self.assertEqual(Find_Max([-1, -2, -3, -4, -5, -6]), -1)
