import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareroot(unittest.TestCase):

    def test_zero_input(self):
        self.assertEqual(babylonian_squareroot(0), 0)

    def test_positive_input(self):
        self.assertAlmostEqual(babylonian_squareroot(9), 3, places=5)

    def test_negative_input(self):
        with self.assertRaises(ZeroDivisionError):
            babylonian_squareroot(-1)

    def test_edge_case_input(self):
        self.assertAlmostEqual(babylonian_squareroot(1), 1, places=5)

    def test_large_input(self):
        self.assertAlmostEqual(babylonian_squareroot(100), 10, places=5)
