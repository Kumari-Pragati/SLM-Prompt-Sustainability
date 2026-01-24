import unittest
from mbpp_246_code import babylonian_squareroot

class TestBabylonianSquareroot(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(babylonian_squareroot(4), 2.0)
        self.assertAlmostEqual(babylonian_squareroot(9), 3.0)
        self.assertAlmostEqual(babylonian_squareroot(25), 5.0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(babylonian_squareroot(0), 0)
        self.assertAlmostEqual(babylonian_squareroot(1), 1.0)
        self.assertAlmostEqual(babylonian_squareroot(2), 1.41421356237)
        self.assertAlmostEqual(babylonian_squareroot(3), 1.73205080757)
        self.assertAlmostEqual(babylonian_squareroot(4.00000000001), 2.00000000001)
        self.assertAlmostEqual(babylonian_squareroot(1000000000000000000), 1000000000000000000.0)
