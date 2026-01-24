import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(is_nonagonal(1), 1)
        self.assertEqual(is_nonagonal(2), 9)
        self.assertEqual(is_nonagonal(3), 16)

    def test_boundary_conditions(self):
        self.assertEqual(is_nonagonal(0), 0)
        self.assertEqual(is_nonagonal(100), 7005)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_nonagonal('a')
        with self.assertRaises(ValueError):
            is_nonagonal(-1)
