import unittest
from mbpp_418_code import Find_Max

class TestFindMax(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 5]), 5)

    def test_edge_case_empty_list(self):
        self.assertIsNone(Find_Max([]))

    def test_boundary_case_single_element(self):
        self.assertEqual(Find_Max([1]), 1)

    def test_boundary_case_negative_numbers(self):
        self.assertEqual(Find_Max([-1, -2, -3, -4, -5]), -1)

    def test_complex_case_duplicate_max(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 4]), 4)

    def test_complex_case_mixed_numbers(self):
        self.assertEqual(Find_Max([-1, 0, 10, 5, -10]), 10)
