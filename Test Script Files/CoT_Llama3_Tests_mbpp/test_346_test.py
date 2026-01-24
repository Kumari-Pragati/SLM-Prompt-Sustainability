import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):
    def test_zero_input(self):
        self.assertEqual(zigzag(0, 0), 1)

    def test_zero_k(self):
        self.assertEqual(zigzag(1, 0), 0)

    def test_nonzero_k(self):
        self.assertEqual(zigzag(2, 1), 2)

    def test_negative_n(self):
        with self.assertRaises(TypeError):
            zigzag(-1, 1)

    def test_negative_k(self):
        with self.assertRaises(TypeError):
            zigzag(1, -1)

    def test_noninteger_n(self):
        with self.assertRaises(TypeError):
            zigzag('a', 1)

    def test_noninteger_k(self):
        with self.assertRaises(TypeError):
            zigzag(1, 'b')
