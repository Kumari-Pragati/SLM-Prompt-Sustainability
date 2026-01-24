import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(move_num('abc123'), 'abc123')
        self.assertEqual(move_num('123abc'), '123abc')
        self.assertEqual(move_num('abc'), 'abc')
        self.assertEqual(move_num('123'), '123')

    def test_empty(self):
        self.assertEqual(move_num(''), '')
        self.assertEqual(move_num('abc'), 'abc')
        self.assertEqual(move_num('123'), '123')

    def test_edge(self):
        self.assertEqual(move_num('a1b2c3'), 'a1b2c3')
        self.assertEqual(move_num('123abc456'), '123abc456')
        self.assertEqual(move_num('abc123abc'), 'abc123abc')

    def test_invalid(self):
        with self.assertRaises(TypeError):
            move_num(None)
        with self.assertRaises(TypeError):
            move_num(123)
