import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(position_min([1, 2, 3, 4, 5]), [0])

    def test_edge_condition_empty_list(self):
        self.assertEqual(position_min([]), [])

    def test_boundary_condition_single_element(self):
        self.assertEqual(position_min([1]), [0])

    def test_edge_condition_all_same_elements(self):
        self.assertEqual(position_min([2, 2, 2, 2]), [0, 1, 2, 3])

    def test_complex_case_multiple_min_values(self):
        self.assertEqual(position_min([2, 1, 2, 1]), [1, 3])

    def test_complex_case_negative_numbers(self):
        self.assertEqual(position_min([-1, -2, -3, -2]), [1, 3])
