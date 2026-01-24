import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareroot(unittest.TestCase):
    def test_positive_number(self):
        self.assertAlmostEqual(babylonian_squareroot(4), 2.0)

    def test_zero(self):
        self.assertEqual(babylonian_squareroot(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            babylonian_squareroot(-1)

    def test_large_number(self):
        self.assertAlmostEqual(babylonian_squareroot(1000000), 1000.0)
