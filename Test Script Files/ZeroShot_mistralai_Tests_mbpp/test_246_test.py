import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareroot(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(babylonian_squareroot(0), 0)

    def test_one(self):
        self.assertAlmostEqual(babylonian_squareroot(1), 1)

    def test_four(self):
        self.assertAlmostEqual(babylonian_squareroot(4), 2)

    def test_nine(self):
        self.assertAlmostEqual(babylonian_squareroot(9), 3)

    def test_negative_one(self):
        with self.assertRaises(ValueError):
            babylonian_squareroot(-1)

    def test_large_number(self):
        self.assertAlmostEqual(babylonian_squareroot(16777216), 128)
