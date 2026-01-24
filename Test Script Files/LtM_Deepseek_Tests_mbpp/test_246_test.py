import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareRoot(unittest.TestCase):

    # Test for simple / typical inputs
    def test_positive_number(self):
        self.assertAlmostEqual(babylonian_squareroot(4), 2.0)
        self.assertAlmostEqual(babylonian_squareroot(9), 3.0)
        self.assertAlmostEqual(babylonian_squareroot(16), 4.0)

    # Test for edge and boundary conditions
    def test_zero(self):
        self.assertEqual(babylonian_squareroot(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            babylonian_squareroot(-1)

    # Test for more complex or corner cases
    def test_large_number(self):
        self.assertAlmostEqual(babylonian_squareroot(1000000), 1000.0)

    def test_decimal_number(self):
        self.assertAlmostEqual(babylonian_squareroot(2.25), 1.5)
