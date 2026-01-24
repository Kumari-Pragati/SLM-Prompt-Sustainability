import unittest
from mbpp_499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(diameter_circle(5), 10)

    def test_boundary_case(self):
        self.assertAlmostEqual(diameter_circle(0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(diameter_circle(0.5), 1)

    def test_negative_case(self):
        with self.assertRaises(ValueError):
            diameter_circle(-5)
