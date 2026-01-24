import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(is_nonagonal(1), 1)
        self.assertEqual(is_nonagonal(2), 4)
        self.assertEqual(is_nonagonal(3), 8)
        self.assertEqual(is_nonagonal(4), 13)
        self.assertEqual(is_nonagonal(5), 18)

    def test_edge_cases(self):
        self.assertEqual(is_nonagonal(0), None)
        self.assertEqual(is_nonagonal(-1), None)
        self.assertEqual(is_nonagonal(0.5), None)
        self.assertEqual(is_nonagonal(-0.5), None)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_nonagonal('a')
        with self.assertRaises(TypeError):
            is_nonagonal(None)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            is_nonagonal(1.5)
        with self.assertRaises(TypeError):
            is_nonagonal(-1.5)
