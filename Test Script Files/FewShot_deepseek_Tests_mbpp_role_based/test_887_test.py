import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(is_odd(3))
        self.assertFalse(is_odd(4))

    def test_boundary_conditions(self):
        self.assertTrue(is_odd(-1))
        self.assertFalse(is_odd(0))
        self.assertTrue(is_odd(1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_odd('a')
        with self.assertRaises(TypeError):
            is_odd(None)
