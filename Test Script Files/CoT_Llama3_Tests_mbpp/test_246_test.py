import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareroot(unittest.TestCase):

    def test_zero_input(self):
        self.assertEqual(babylonian_squareroot(0), 0)

    def test_positive_input(self):
        self.assertAlmostEqual(babylonian_squareroot(9), 3)
        self.assertAlmostEqual(babylonian_squareroot(16), 4)
        self.assertAlmostEqual(babylonian_squareroot(25), 5)

    def test_negative_input(self):
        with self.assertRaises(OverflowError):
            babylonian_squareroot(-1)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            babylonian_squareroot('a')

    def test_edge_cases(self):
        self.assertAlmostEqual(babylonian_squareroot(1), 1)
        self.assertAlmostEqual(babylonian_squareroot(4), 2)
