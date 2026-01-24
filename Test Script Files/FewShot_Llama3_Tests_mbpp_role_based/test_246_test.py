import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareroot(unittest.TestCase):
    def test_positive_number(self):
        self.assertAlmostEqual(babylonian_squareroot(9), 3)

    def test_zero(self):
        self.assertEqual(babylonian_squareroot(0), 0)

    def test_negative_number(self):
        self.assertAlmostEqual(babylonian_squareroot(-9), 3)

    def test_non_integer_number(self):
        self.assertAlmostEqual(babylonian_squareroot(4.5), 2.121)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            babylonian_squareroot('a')
