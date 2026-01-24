import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareroot(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(babylonian_squareroot(1), 1)
        self.assertAlmostEqual(babylonian_squareroot(4), 2)
        self.assertAlmostEqual(babylonian_squareroot(9), 3)
        self.assertAlmostEqual(babylonian_squareroot(25), 5)
        self.assertAlmostEqual(babylonian_squareroot(16), 4)

    def test_zero(self):
        self.assertEqual(babylonian_squareroot(0), 0)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, babylonian_squareroot, -1)
        self.assertRaises(ValueError, babylonian_squareroot, -4)
        self.assertRaises(ValueError, babylonian_squareroot, -9)
        self.assertRaises(ValueError, babylonian_squareroot, -25)
        self.assertRaises(ValueError, babylonian_squareroot, -16)
