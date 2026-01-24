import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertAlmostEqual(slope(1,2,3,4), 1.0)
        self.assertAlmostEqual(slope(2,4,4,6), 1.0)
        self.assertAlmostEqual(slope(-1,-2,1,0), 1.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(slope(0,0,0,0), float('inf'))
        self.assertAlmostEqual(slope(1,1,1,1), 0.0)
        self.assertAlmostEqual(slope(-1,-1,1,1), float('-inf'))

    def test_invalid_inputs(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1,2,1,2)
        with self.assertRaises(ZeroDivisionError):
            slope(1,1,1,1)

    def test_boundary_cases(self):
        self.assertAlmostEqual(slope(-100,-50,100,50), 1.0)
        self.assertAlmostEqual(slope(-100,50,100,-50), -1.0)
