import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareroot(unittest.TestCase):
    def test_typical_cases(self):
        self.assertAlmostEqual(babylonian_squareroot(1), 1)
        self.assertAlmostEqual(babylonian_squareroot(4), 2)
        self.assertAlmostEqual(babylonian_squareroot(9), 3)
        self.assertAlmostEqual(babylonian_squareroot(25), 5)
        self.assertAlmostEqual(babylonian_squareroot(16), 4)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(babylonian_squareroot(0), 0)
        self.assertAlmostEqual(babylonian_squareroot(1.000000001), 1)
        self.assertAlmostEqual(babylonian_squareroot(2), 1.4142135623730951)
        self.assertAlmostEqual(babylonian_squareroot(3), 1.7320508075688772)
