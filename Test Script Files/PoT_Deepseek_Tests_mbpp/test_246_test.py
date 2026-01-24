import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareRoot(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(babylonian_squareroot(4), 2.0, places=1)
        self.assertAlmostEqual(babylonian_squareroot(9), 3.0, places=1)
        self.assertAlmostEqual(babylonian_squareroot(16), 4.0, places=1)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(babylonian_squareroot(0), 0.0, places=1)
        self.assertAlmostEqual(babylonian_squareroot(1), 1.0, places=1)
        self.assertAlmostEqual(babylonian_squareroot(2), 1.41421356237, places=10)

    def test_corner_cases(self):
        self.assertAlmostEqual(babylonian_squareroot(0.25), 0.5, places=1)
        self.assertAlmostEqual(babylonian_squareroot(0.64), 0.8, places=1)
        self.assertAlmostEqual(babylonian_squareroot(0.01), 0.1, places=1)
