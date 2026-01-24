import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):

    def test_same_length(self):
        self.assertTrue(same_Length(123, 456))
        self.assertTrue(same_Length(123, 123))
        self.assertTrue(same_Length(0, 0))
        self.assertFalse(same_Length(123, 0))
        self.assertFalse(same_Length(0, 456))
        self.assertFalse(same_Length(123, 789))

    def test_edge_cases(self):
        self.assertTrue(same_Length(10, 10))
        self.assertTrue(same_Length(1, 1))
        self.assertFalse(same_Length(10, 1))
        self.assertFalse(same_Length(1, 10))

    def test_zero_input(self):
        self.assertTrue(same_Length(0, 0))
        self.assertFalse(same_Length(0, 123))
        self.assertFalse(same_Length(123, 0))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            same_Length('123', 456)
        with self.assertRaises(TypeError):
            same_Length(123, '456')
