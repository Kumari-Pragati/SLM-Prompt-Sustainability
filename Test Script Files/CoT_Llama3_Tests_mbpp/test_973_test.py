import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(left_rotate('hello', 2), 'llohe')

    def test_edge_case(self):
        self.assertEqual(left_rotate('hello', 5), 'hello')

    def test_edge_case2(self):
        self.assertEqual(left_rotate('hello', 0), 'hello')

    def test_edge_case3(self):
        self.assertEqual(left_rotate('hello', 6), 'hello')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            left_rotate(123, 2)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            left_rotate('hello', 'a')

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            left_rotate([], 2)

    def test_invalid_input4(self):
        with self.assertRaises(TypeError):
            left_rotate('hello', -1)
