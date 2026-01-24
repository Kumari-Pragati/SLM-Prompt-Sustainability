import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(area_trapezium(5, 10, 3), 37.5)

    def test_edge_cases(self):
        self.assertEqual(area_trapezium(0, 10, 3), 15)
        self.assertEqual(area_trapezium(5, 0, 3), 7.5)
        self.assertEqual(area_trapezium(5, 10, 0), 0)

    def test_negative_inputs(self):
        self.assertEqual(area_trapezium(-5, 10, 3), 22.5)
        self.assertEqual(area_trapezium(5, -10, 3), 7.5)
        self.assertEqual(area_trapezium(-5, -10, 3), 15)

    def test_zero_inputs(self):
        self.assertEqual(area_trapezium(0, 0, 3), 0)
        self.assertEqual(area_trapezium(0, 10, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            area_trapezium('a', 10, 3)
        with self.assertRaises(TypeError):
            area_trapezium(5, 'b', 3)
        with self.assertRaises(TypeError):
            area_trapezium(5, 10, 'c')
