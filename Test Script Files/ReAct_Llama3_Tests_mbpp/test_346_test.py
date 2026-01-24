import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):

    def test_zero_input(self):
        self.assertEqual(zigzag(0, 0), 1)

    def test_zero_k(self):
        self.assertEqual(zigzag(5, 0), 0)

    def test_nonzero_k(self):
        self.assertEqual(zigzag(5, 3), zigzag(2, 0) + zigzag(3, 2))

    def test_nonzero_n(self):
        self.assertEqual(zigzag(5, 3), zigzag(2, 0) + zigzag(3, 2))

    def test_negative_k(self):
        with self.assertRaises(TypeError):
            zigzag(5, -1)

    def test_negative_n(self):
        with self.assertRaises(TypeError):
            zigzag(-5, 3)
