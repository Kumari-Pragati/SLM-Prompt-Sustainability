import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):

    def test_same_length_normal(self):
        self.assertTrue(same_Length(1234, 5678))
        self.assertTrue(same_Length(0.0123, 0.4567))
        self.assertTrue(same_Length(123, 123000))

    def test_same_length_edge_cases(self):
        self.assertTrue(same_Length(0, 0))
        self.assertFalse(same_Length(0, 1))
        self.assertFalse(same_Length(1, 0))

    def test_same_length_boundary(self):
        self.assertTrue(same_Length(9999, 9999))
        self.assertFalse(same_Length(10000, 9999))
        self.assertFalse(same_Length(9999, 10000))

    def test_same_length_invalid_inputs(self):
        self.assertRaises(TypeError, same_Length, 'abc', 123)
        self.assertRaises(TypeError, same_Length, 123, 'abc')
