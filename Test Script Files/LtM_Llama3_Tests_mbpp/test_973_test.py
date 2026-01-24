import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(left_rotate('hello', 2), 'llohe')

    def test_edge1(self):
        self.assertEqual(left_rotate('hello', 0), 'hello')

    def test_edge2(self):
        self.assertEqual(left_rotate('hello', 5), 'hello')

    def test_edge3(self):
        self.assertEqual(left_rotate('', 0), '')

    def test_edge4(self):
        self.assertEqual(left_rotate('', 1), '')

    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            left_rotate(123, 2)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            left_rotate('hello', 'abc')

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            left_rotate('hello', -1)
