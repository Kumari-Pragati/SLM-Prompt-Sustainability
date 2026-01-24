import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareroot(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(babylonian_squareroot(4), 2.0, places=1)
        self.assertAlmostEqual(babylonian_squareroot(9), 3.0, places=1)
        self.assertAlmostEqual(babylonian_squareroot(16), 4.0, places=1)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(babylonian_squareroot(0), 0.0, places=1)
        self.assertAlmostEqual(babylonian_squareroot(1), 1.0, places=1)
        self.assertAlmostEqual(babylonian_squareroot(2), 1.41421356237, places=10)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            babylonian_squareroot('a')
        with self.assertRaises(TypeError):
            babylonian_squareroot(None)
        with self.assertRaises(TypeError):
            babylonian_squareroot([1, 2, 3])
