import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareroot(unittest.TestCase):
    def test_zero_input(self):
        self.assertEqual(babylonian_squareroot(0), 0)

    def test_positive_input(self):
        self.assertAlmostEqual(babylonian_squareroot(4), 2)

    def test_negative_input(self):
        self.assertAlmostEqual(babylonian_squareroot(-4), -2)

    def test_edge_case_zero_input(self):
        self.assertEqual(babylonian_squareroot(0), 0)

    def test_edge_case_negative_input(self):
        self.assertAlmostEqual(babylonian_squareroot(-9), -3)

    def test_edge_case_positive_input(self):
        self.assertAlmostEqual(babylonian_squareroot(9), 3)

    def test_edge_case_zero_output(self):
        self.assertEqual(babylonian_squareroot(0), 0)

    def test_edge_case_negative_output(self):
        self.assertAlmostEqual(babylonian_squareroot(-9), -3)

    def test_edge_case_positive_output(self):
        self.assertAlmostEqual(babylonian_squareroot(9), 3)

    def test_edge_case_zero_input_output(self):
        self.assertEqual(babylonian_squareroot(0), 0)

    def test_edge_case_negative_input_output(self):
        self.assertAlmostEqual(babylonian_squareroot(-9), -3)

    def test_edge_case_positive_input_output(self):
        self.assertAlmostEqual(babylonian_squareroot(9), 3)
