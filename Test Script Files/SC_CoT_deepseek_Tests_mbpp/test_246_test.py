import unittest

from mbpp_246_code import babylonian_squareroot

class BabylonianSquareRootTest(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(babylonian_squareroot(4), 2.0, places=5)

    def test_zero(self):
        self.assertEqual(babylonian_squareroot(0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(babylonian_squareroot(1), 1.0, places=5)

    def test_large_number(self):
        self.assertAlmostEqual(babylonian_squareroot(10000), 100.0, places=5)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            babylonian_squareroot(-1)
