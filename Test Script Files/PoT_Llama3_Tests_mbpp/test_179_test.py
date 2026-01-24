import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_num_keith(123))
        self.assertTrue(is_num_keith(456))
        self.assertTrue(is_num_keith(789))

    def test_edge_cases(self):
        self.assertFalse(is_num_keith(0))
        self.assertFalse(is_num_keith(1))
        self.assertFalse(is_num_keith(2))

    def test_boundary_cases(self):
        self.assertTrue(is_num_keith(111))
        self.assertTrue(is_num_keith(222))
        self.assertTrue(is_num_keith(333))

    def test_corner_cases(self):
        self.assertFalse(is_num_keith(123456))
        self.assertFalse(is_num_keith(789012))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_num_keith('abc')
        with self.assertRaises(TypeError):
            is_num_keith(None)
