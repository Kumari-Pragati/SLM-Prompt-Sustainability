import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(is_nonagonal(1), 1)
        self.assertEqual(is_nonagonal(2), 10)
        self.assertEqual(is_nonagonal(3), 22)
        self.assertEqual(is_nonagonal(4), 37)

    def test_edge_cases(self):
        self.assertEqual(is_nonagonal(0), 0)
        self.assertEqual(is_nonagonal(-1), -1)

    def test_boundary_cases(self):
        self.assertEqual(is_nonagonal(100), 3495)
        self.assertEqual(is_nonagonal(200), 13990)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_nonagonal('a')
        with self.assertRaises(TypeError):
            is_nonagonal(None)
        with self.assertRaises(TypeError):
            is_nonagonal([1, 2, 3])
