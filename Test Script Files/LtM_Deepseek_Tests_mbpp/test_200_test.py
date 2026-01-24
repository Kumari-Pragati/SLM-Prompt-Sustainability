import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(position_max([1, 2, 3, 4, 5]), [4])

    def test_edge_case_empty_list(self):
        self.assertEqual(position_max([]), [])

    def test_boundary_case_single_element(self):
        self.assertEqual(position_max([1]), [0])

    def test_edge_case_all_same_elements(self):
        self.assertEqual(position_max([3, 3, 3, 3]), [0, 1, 2, 3])

    def test_complex_case_multiple_max_values(self):
        self.assertEqual(position_max([1, 2, 3, 3, 4, 5]), [2, 3])

    def test_complex_case_negative_numbers(self):
        self.assertEqual(position_max([-1, -2, -3, -4, -5]), [0])

    def test_complex_case_mixed_numbers(self):
        self.assertEqual(position_max([-1, 2, -3, 4, 5]), [3, 4, 5])
