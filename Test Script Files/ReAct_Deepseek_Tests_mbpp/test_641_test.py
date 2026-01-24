import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(is_nonagonal(1), 1)
        self.assertEqual(is_nonagonal(2), 10)
        self.assertEqual(is_nonagonal(3), 22)
        self.assertEqual(is_nonagonal(4), 37)
        self.assertEqual(is_nonagonal(5), 55)

    def test_boundary_cases(self):
        self.assertEqual(is_nonagonal(0), 0)
        self.assertEqual(is_nonagonal(100), 3975)
        self.assertEqual(is_nonagonal(1000), 399749)

    def test_negative_cases(self):
        with self.assertRaises(ValueError):
            is_nonagonal(-1)
        with self.assertRaises(ValueError):
            is_nonagonal(-100)
