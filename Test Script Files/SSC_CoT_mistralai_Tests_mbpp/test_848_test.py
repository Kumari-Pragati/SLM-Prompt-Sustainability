import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(area_trapezium(3, 4, 5), 15.0)
        self.assertEqual(area_trapezium(1, 1, 2), 2.0)
        self.assertEqual(area_trapezium(5, 5, 10), 50.0)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(area_trapezium(0, 1, 1), 0.5, delta=0.01)
        self.assertAlmostEqual(area_trapezium(1, 0, 1), 0.5, delta=0.01)
        self.assertAlmostEqual(area_trapezium(1, 1, 0), 0.0, delta=0.01)
        self.assertEqual(area_trapezium(1, 1, 0), 0.0)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, area_trapezium, -1, 1, 1)
        self.assertRaises(ValueError, area_trapezium, 1, -1, 1)
        self.assertRaises(ValueError, area_trapezium, 1, 1, 0)
