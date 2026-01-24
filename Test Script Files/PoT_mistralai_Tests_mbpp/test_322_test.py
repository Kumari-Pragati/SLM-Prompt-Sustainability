import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(position_min([1, 2, 3, 2, 1]), [1, 4])
        self.assertEqual(position_min([-1, -2, -3, -2, -1]), [3, 4])
        self.assertEqual(position_min([0, 0, 0]), [0, 1, 2])

    def test_edge_case_single_element(self):
        self.assertEqual(position_min([1]), [0])
        self.assertEqual(position_min([-1]), [0])

    def test_edge_case_empty_list(self):
        self.assertEqual(position_min([]), [])

    def test_corner_case_duplicate_min_values(self):
        self.assertEqual(position_min([1, 1, 2, 1]), [0, 2])
        self.assertEqual(position_min([-1, -1, -2, -1]), [0, 2])
