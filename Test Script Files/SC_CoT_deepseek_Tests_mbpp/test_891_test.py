import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(same_Length(123, 12345))

    def test_edge_case(self):
        self.assertTrue(same_Length(0, 0))
        self.assertFalse(same_Length(123, 0))
        self.assertFalse(same_Length(0, 123))

    def test_boundary_case(self):
        self.assertTrue(same_Length(10**9, 10**9))
        self.assertFalse(same_Length(10**9+1, 10**9))
        self.assertFalse(same_Length(10**9, 10**9+1))

    def test_special_case(self):
        self.assertFalse(same_Length(123, 456))
        self.assertFalse(same_Length(12345, 123))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            same_Length("123", 123)
        with self.assertRaises(TypeError):
            same_Length(123, "123")
        with self.assertRaises(TypeError):
            same_Length("123", "123")
