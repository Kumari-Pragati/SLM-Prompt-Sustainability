import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(slope(1,2,3,4), 1.0)

    def test_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1,2,1,2)

    def test_negative_inputs(self):
        self.assertEqual(slope(-1,-2,-3,-4), -1.0)

    def test_edge_cases(self):
        self.assertEqual(slope(0,0,0,0), float('inf'))
        self.assertEqual(slope(0,0,1,0), float('-inf'))
        self.assertEqual(slope(1,0,0,0), float('inf'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            slope('a','b','c','d')
        with self.assertRaises(TypeError):
            slope(1,'b',3,'d')
