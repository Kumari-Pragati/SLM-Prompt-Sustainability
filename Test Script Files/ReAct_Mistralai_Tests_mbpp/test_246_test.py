import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareroot(unittest.TestCase):

    def test_positive_numbers(self):
        for number in [1, 4, 9, 25, 100]:
            self.assertAlmostEqual(babylonian_squareroot(number), number**0.5)

    def test_zero(self):
        self.assertEqual(babylonian_squareroot(0), 0)

    def test_negative_numbers(self):
        for number in [-1, -4, -9, -25, -100]:
            with self.assertRaises(ValueError):
                babylonian_squareroot(number)

    def test_float_numbers(self):
        for number in [2.25, 3.0625, 4.14]:
            self.assertAlmostEqual(babylonian_squareroot(number), number**0.5)
