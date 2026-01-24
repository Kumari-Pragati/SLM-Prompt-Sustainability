import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):

    def test_move_num(self):
        self.assertEqual(move_num('a1b2c3'), 'abc123')
        self.assertEqual(move_num('1a2b3c'), '1a2b3c')
        self.assertEqual(move_num('123abc'), '123abc')
        self.assertEqual(move_num('a1b2c3d4e5f6'), 'abcdef123456')
        self.assertEqual(move_num(''), '')
        self.assertEqual(move_num('123456'), '123456')
        self.assertEqual(move_num('abc'), 'abc')
