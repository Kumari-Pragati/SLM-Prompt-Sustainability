import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareroot(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(babylonian_squareroot(9), 3)
        self.assertEqual(babylonian_squareroot(16), 4)
        self.assertEqual(babylonian_squareroot(25), 5)
        self.assertEqual(babylonian_squareroot(36), 6)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(babylonian_squareroot(0), 0)
        self.assertEqual(babylonian_squareroot(1), 1)
        self.assertEqual(babylonian_squareroot(4), 2)
        self.assertEqual(babylonian_squareroot(9), 3)

    def test_special_and_corner_cases(self):
        self.assertEqual(babylonian_squareroot(2), 1.4142135623746899)
        self.assertEqual(babylonian_squareroot(3), 1.7320508075688772)
        self.assertEqual(babylonian_squareroot(4), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(ZeroDivisionError):
            babylonian_squareroot(-1)
        with self.assertRaises(ZeroDivisionError):
            babylonian_squareroot(-9)
        with self.assertRaises(ZeroDivisionError):
            babylonian_squareroot(-16)
