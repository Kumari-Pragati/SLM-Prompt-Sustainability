import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(perimeter(5, 10), 30)
        self.assertAlmostEqual(perimeter(7.5, 15), 45)

    def test_edge_cases(self):
        self.assertAlmostEqual(perimeter(0, 0), 0)
        self.assertAlmostEqual(perimeter(1, 0), 2)
        self.assertAlmostEqual(perimeter(0, 1), 2)

    def test_corner_cases(self):
        self.assertAlmostEqual(perimeter(1000000000000000, 1000000000000000), 4000000000000000)
        self.assertAlmostEqual(perimeter(0.0000000000000001, 0.0000000000000001), 2)
