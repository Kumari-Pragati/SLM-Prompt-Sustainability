import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareroot(unittest.TestCase):

    def test_simple(self):
        self.assertAlmostEqual(babylonian_squareroot(1), 1)
        self.assertAlmostEqual(babylonian_squareroot(4), 2)
        self.assertAlmostEqual(babylonian_squareroot(9), 3)

    def test_edge_and_boundary(self):
        self.assertEqual(babylonian_squareroot(0), 0)
        self.assertAlmostEqual(babylonian_squareroot(1.000000001), 1)
        self.assertAlmostEqual(babylonian_squareroot(16), 4)
        self.assertAlmostEqual(babylonian_squareroot(256), 16)

    def test_complex(self):
        self.assertAlmostEqual(babylonian_squareroot(0.25), 0.5)
        self.assertAlmostEqual(babylonian_squareroot(2.23456789), 1.5023456789)
        self.assertAlmostEqual(babylonian_squareroot(3.141592653589793), 1.772453159265359)
