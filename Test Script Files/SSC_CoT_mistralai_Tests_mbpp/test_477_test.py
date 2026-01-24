import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):
    def test_normal_input(self):
        self.assertTrue(is_lower("hello"))
        self.assertTrue(is_lower("Python"))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(is_lower(""))
        self.assertTrue(is_lower("A"))
        self.assertTrue(is_lower("abcdefghijklmnopqrstuvwxyz"))
        self.assertTrue(is_lower("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertTrue(is_lower("abcdefghijklmnopqrstuvwxyz0123456789"))
        self.assertTrue(is_lower("abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[]{}|;:'\",.<>/?"))

    def test_invalid_input(self):
        self.assertRaises(TypeError, is_lower, 123)
        self.assertRaises(TypeError, is_lower, None)
        self.assertRaises(TypeError, is_lower, [])
