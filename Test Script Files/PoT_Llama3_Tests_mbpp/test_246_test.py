import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareroot(unittest.TestCase):
    def test_typical_cases(self):
        self.assertAlmostEqual(babylonian_squareroot(4), 2.0)
        self.assertAlmostEqual(babylonian_squareroot(9), 3.0)
        self.assertAlmostEqual(babylonian_squareroot(16), 4.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(babylonian_squareroot(0), 0.0)
        self.assertAlmostEqual(babylonian_squareroot(1), 1.0)

    def test_invalid_inputs(self):
        with self.assertRaises(ZeroDivisionError):
            babylonian_squareroot(-1)

    def test_boundary_cases(self):
        self.assertAlmostEqual(babylonian_squareroot(2), 1.4142135623746899)
        self.assertAlmostEqual(babylonian_squareroot(3), 1.7320508075688772)
