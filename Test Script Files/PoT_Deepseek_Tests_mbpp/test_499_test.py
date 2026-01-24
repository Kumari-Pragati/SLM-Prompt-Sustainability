import unittest
from mbpp_499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(diameter_circle(5), 10)
        self.assertAlmostEqual(diameter_circle(10), 20)

    def test_edge_cases(self):
        self.assertAlmostEqual(diameter_circle(0), 0)

    def test_boundary_cases(self):
        self.assertAlmostEqual(diameter_circle(1), 2)
        self.assertAlmostEqual(diameter_circle(100), 200)
