import unittest
from mbpp_246_code import babylonian_squareroot

class BabylonianSquareRootTest(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertAlmostEqual(babylonian_squareroot(4), 2.0, places=1)
        self.assertAlmostEqual(babylonian_squareroot(9), 3.0, places=1)
        self.assertAlmostEqual(babylonian_squareroot(16), 4.0, places=1)
        self.assertAlmostEqual(babylonian_squareroot(25), 5.0, places=1)

    def test_zero(self):
        self.assertEqual(babylonian_squareroot(0), 0)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            babylonian_squareroot(-1)

    def test_large_numbers(self):
        self.assertAlmostEqual(babylonian_squareroot(10000), 100.0, places=1)
        self.assertAlmostEqual(babylonian_squareroot(100000000), 10000.0, places=1)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(babylonian_squareroot(2.25), 1.5, places=1)
        self.assertAlmostEqual(babylonian_squareroot(3.61), 1.9, places=1)
