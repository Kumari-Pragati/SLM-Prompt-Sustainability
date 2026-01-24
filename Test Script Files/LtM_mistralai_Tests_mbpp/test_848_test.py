import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(area_trapezium(1, 2, 3), 6.0)
        self.assertEqual(area_trapezium(2, 2, 1), 2.0)
        self.assertEqual(area_trapezium(3, 4, 5), 15.0)

    def test_edge_cases(self):
        self.assertEqual(area_trapezium(0, 1, 1), 0.5)
        self.assertEqual(area_trapezium(1, 0, 1), 0.5)
        self.assertEqual(area_trapezium(1, 1, 0), 0.0)
        self.assertEqual(area_trapezium(1, 1, 1), 0.5)

    def test_negative_and_zero_inputs(self):
        self.assertEqual(area_trapezium(-1, 2, 3), 3.0)
        self.assertEqual(area_trapezium(1, -2, 3), 3.0)
        self.assertEqual(area_trapezium(1, 2, -3), 0.0)
        self.assertEqual(area_trapezium(0, 0, 0), 0.0)
