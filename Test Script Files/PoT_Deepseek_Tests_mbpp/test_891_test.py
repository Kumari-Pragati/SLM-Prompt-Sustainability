import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(same_Length(123, 12345))
        self.assertTrue(same_Length(12345, 123))
        self.assertFalse(same_Length(12345, 1234))

    def test_edge_cases(self):
        self.assertTrue(same_Length(0, 0))
        self.assertFalse(same_Length(0, 123))
        self.assertFalse(same_Length(123, 0))

    def test_boundary_cases(self):
        self.assertTrue(same_Length(1, 10))
        self.assertFalse(same_Length(10, 1))
        self.assertFalse(same_Length(10, 100))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            same_Length("123", 123)
        with self.assertRaises(TypeError):
            same_Length(123, "123")
        with self.assertRaises(TypeError):
            same_Length("123", "123")
