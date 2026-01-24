import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(left_rotate("hello", 2), "llohe")

    def test_edge_case1(self):
        self.assertEqual(left_rotate("hello", 5), "hello")

    def test_edge_case2(self):
        self.assertEqual(left_rotate("hello", 0), "hello")

    def test_edge_case3(self):
        self.assertEqual(left_rotate("hello", 1), "elloh")

    def test_edge_case4(self):
        self.assertEqual(left_rotate("hello", 6), "hello")

    def test_edge_case5(self):
        self.assertEqual(left_rotate("hello", 7), "hello")

    def test_error_case1(self):
        with self.assertRaises(TypeError):
            left_rotate(123, 2)

    def test_error_case2(self):
        with self.assertRaises(TypeError):
            left_rotate("hello", "a")

    def test_error_case3(self):
        with self.assertRaises(TypeError):
            left_rotate(None, 2)

    def test_error_case4(self):
        with self.assertRaises(TypeError):
            left_rotate("hello", None)
