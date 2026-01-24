import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(position_min([1, 2, 3, 4, 5]), [0])

    def test_edge_case_single_element(self):
        self.assertEqual(position_min([1]), [0])

    def test_boundary_case_duplicate_min(self):
        self.assertEqual(position_min([2, 1, 1]), [1, 2])

    def test_corner_case_empty_list(self):
        self.assertEqual(position_min([]), [])

    def test_corner_case_negative_numbers(self):
        self.assertEqual(position_min([-1, -2, -3]), [0, 1, 2])

    def test_corner_case_mixed_numbers(self):
        self.assertEqual(position_min([5, 3, 2, 1, 4]), [3])
