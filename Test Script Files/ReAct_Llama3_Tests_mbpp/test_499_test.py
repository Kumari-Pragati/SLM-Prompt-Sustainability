import unittest
from mbpp_499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):
    def test_typical_radius(self):
        self.assertEqual(diameter_circle(5), 10)

    def test_zero_radius(self):
        with self.assertRaises(TypeError):
            diameter_circle(0)

    def test_negative_radius(self):
        with self.assertRaises(TypeError):
            diameter_circle(-5)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            diameter_circle('five')

    def test_edge_radius(self):
        self.assertEqual(diameter_circle(1), 2)

    def test_max_radius(self):
        self.assertEqual(diameter_circle(1000), 2000)
