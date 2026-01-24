import unittest
from mbpp_246_code import babylonian_squareroot

class BabylonianSquareRootTest(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(babylonian_squareroot(0), 0)

    def test_positive_numbers(self):
        self.assertAlmostEqual(babylonian_squareroot(2), 1.41421356237, places=7)
        self.assertAlmostEqual(babylonian_squareroot(4), 2.0, places=7)
        self.assertAlmostEqual(babylonian_squareroot(16), 4.0, places=7)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            babylonian_squareroot(-1)
