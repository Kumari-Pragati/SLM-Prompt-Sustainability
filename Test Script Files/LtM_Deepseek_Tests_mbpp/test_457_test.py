import unittest
from mbpp_457_code import Find_Min

class TestFindMin(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(Find_Min([1, 2, 3, 4, 5]), 1)

    def test_edge_condition_empty_list(self):
        self.assertIsNone(Find_Min([]))

    def test_boundary_condition_single_element(self):
        self.assertEqual(Find_Min([1]), 1)

    def test_complex_input_with_duplicates(self):
        self.assertEqual(Find_Min([5, 2, 3, 4, 1, 1]), 1)

    def test_complex_input_with_negative_numbers(self):
        self.assertEqual(Find_Min([-5, -2, -3, -4, -1]), -5)

    def test_complex_input_with_mixed_numbers(self):
        self.assertEqual(Find_Min([5, -2, 3, -4, 1]), -4)
