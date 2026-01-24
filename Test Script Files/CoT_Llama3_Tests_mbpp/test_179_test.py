import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):
    def test_typical(self):
        self.assertTrue(is_num_keith(123))
        self.assertTrue(is_num_keith(456))
        self.assertTrue(is_num_keith(789))

    def test_edge(self):
        self.assertFalse(is_num_keith(0))
        self.assertFalse(is_num_keith(1))
        self.assertFalse(is_num_keith(2))

    def test_invalid(self):
        with self.assertRaises(TypeError):
            is_num_keith('abc')
        with self.assertRaises(TypeError):
            is_num_keith(None)

    def test_boundary(self):
        self.assertFalse(is_num_keith(10))
        self.assertFalse(is_num_keith(20))
        self.assertFalse(is_num_keith(30))
