import unittest
from mbpp_600_code import is_Even

class TestIsEven(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(is_Even(4))
        self.assertFalse(is_Even(5))

    def test_boundary_conditions(self):
        self.assertTrue(is_Even(0))
        self.assertFalse(is_Even(1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Even('a')
        with self.assertRaises(TypeError):
            is_Even(None)
