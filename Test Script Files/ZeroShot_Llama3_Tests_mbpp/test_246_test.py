import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareroot(unittest.TestCase):

    def test_babylonian_squareroot_positive(self):
        self.assertAlmostEqual(babylonian_squareroot(9), 3, places=5)

    def test_babylonian_squareroot_negative(self):
        self.assertAlmostEqual(babylonian_squareroot(-9), 3, places=5)

    def test_babylonian_squareroot_zero(self):
        self.assertAlmostEqual(babylonian_squareroot(0), 0, places=5)

    def test_babylonian_squareroot_non_integer(self):
        self.assertAlmostEqual(babylonian_squareroot(2.25), 1.5, places=5)

    def test_babylonian_squareroot_edge_case(self):
        self.assertAlmostEqual(babylonian_squareroot(1), 1, places=5)
