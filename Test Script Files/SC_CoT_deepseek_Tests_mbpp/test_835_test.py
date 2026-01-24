import unittest

from mbpp_835_code import slope

class TestSlopeFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(slope(1, 2, 4, 8), 2.0)

    def test_edge_case_horizontal_line(self):
        self.assertEqual(slope(1, 2, 1, 3), 0)

    def test_edge_case_vertical_line(self):
        self.assertEqual(slope(1, 2, 2, 2), float('inf'))

    def test_boundary_case_same_points(self):
        self.assertIsNone(slope(1, 2, 1, 2))

    def test_invalid_input_same_x_coordinates(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1, 2, 1, 3)

    def test_invalid_input_same_y_coordinates(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1, 1, 2, 1)
