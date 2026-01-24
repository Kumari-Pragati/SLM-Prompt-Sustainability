import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertTrue(is_num_decagonal(1))
        self.assertTrue(is_num_decagonal(2))
        self.assertTrue(is_num_decagonal(3))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(is_num_decagonal(0))
        self.assertFalse(is_num_decagonal(-1))
        self.assertFalse(is_num_decagonal(-2))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_num_decagonal('a')
        with self.assertRaises(TypeError):
            is_num_decagonal(None)
