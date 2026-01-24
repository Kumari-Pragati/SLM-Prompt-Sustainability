import unittest
from mbpp_499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(diameter_circle(5), 10)

    def test_boundary_conditions(self):
        self.assertEqual(diameter_circle(0), 0)
        self.assertEqual(diameter_circle(1), 2)

    def test_edge_conditions(self):
        self.assertEqual(diameter_circle(float('inf')), float('inf'))
        self.assertEqual(diameter_circle(-1), -2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            diameter_circle('a')
        with self.assertRaises(ValueError):
            diameter_circle(-5)
