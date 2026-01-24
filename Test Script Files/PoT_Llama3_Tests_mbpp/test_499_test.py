import unittest
from mbpp_499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(diameter_circle(5), 10)

    def test_edge_case_zero_radius(self):
        self.assertEqual(diameter_circle(0), 0)

    def test_edge_case_negative_radius(self):
        with self.assertRaises(TypeError):
            diameter_circle(-1)

    def test_edge_case_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            diameter_circle('a')

    def test_edge_case_large_radius(self):
        self.assertEqual(diameter_circle(1000), 2000)

    def test_edge_case_max_radius(self):
        self.assertEqual(diameter_circle(float('inf')), float('inf'))
