import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):
    def test_zero_input(self):
        self.assertEqual(zigzag(0, 0), 1)

    def test_zero_k(self):
        self.assertEqual(zigzag(1, 0), 0)

    def test_base_case(self):
        self.assertEqual(zigzag(1, 1), 1)

    def test_recursive_case(self):
        self.assertEqual(zigzag(2, 1), 2)

    def test_negative_n(self):
        with self.assertRaises(TypeError):
            zigzag(-1, 1)

    def test_negative_k(self):
        with self.assertRaises(TypeError):
            zigzag(1, -1)

    def test_non_integer_n(self):
        with self.assertRaises(TypeError):
            zigzag('a', 1)

    def test_non_integer_k(self):
        with self.assertRaises(TypeError):
            zigzag(1, 'b')
