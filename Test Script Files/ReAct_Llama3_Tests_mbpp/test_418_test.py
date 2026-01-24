import unittest
from mbpp_418_code import Find_Max

class TestFind_Max(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 5]), 5)

    def test_edge_case_empty_list(self):
        self.assertRaises(ValueError, Find_Max, [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(Find_Max([10]), 10)

    def test_edge_case_all_equal_elements(self):
        self.assertEqual(Find_Max([5, 5, 5, 5, 5]), 5)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(Find_Max([-5, -3, -1, 0, 2]), 2)

    def test_edge_case_mixed_positive_negative(self):
        self.assertEqual(Find_Max([-5, -3, -1, 0, 2, 5]), 5)
