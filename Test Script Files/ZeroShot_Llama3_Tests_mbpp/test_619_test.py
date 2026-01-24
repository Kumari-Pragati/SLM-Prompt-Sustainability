import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):

    def test_move_num(self):
        self.assertEqual(move_num('abc123'), 'abc123')
        self.assertEqual(move_num('abc123def'), 'abc123def')
        self.assertEqual(move_num('abc123def456'), 'abc123def456')
        self.assertEqual(move_num('abc123def456ghi'), 'abc123def456ghi')
        self.assertEqual(move_num('abc123def456ghi789'), 'abc123def456ghi789')
        self.assertEqual(move_num('abc123def456ghi789abc'), 'abc123def456ghi789abc')
        self.assertEqual(move_num('abc123def456ghi789abc123'), 'abc123def456ghi789abc123')
        self.assertEqual(move_num('abc123def456ghi789abc123def'), 'abc123def456ghi789abc123def')
        self.assertEqual(move_move('abc123def456ghi789abc123def456'), 'abc123def456ghi789abc123def456')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi'), 'abc123def456ghi789abc123def456ghi')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789'), 'abc123def456ghi789abc123def456ghi789')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789abc'), 'abc123def456ghi789abc123def456ghi789abc')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789abc123'), 'abc123def456ghi789abc123def456ghi789abc123')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789abc123def'), 'abc123def456ghi789abc123def456ghi789abc123def')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789abc123def456'), 'abc123def456ghi789abc123def456ghi789abc123def456')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789abc123def456ghi'), 'abc123def456ghi789abc123def456ghi789abc123def456ghi')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789abc123def456ghi789'), 'abc123def456ghi789abc123def456ghi789abc123def456ghi789')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789abc123def456ghi789abc'), 'abc123def456ghi789abc123def456ghi789abc123def456ghi789abc')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123'), 'abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def'), 'abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def456'), 'abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def456')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def456ghi'), 'abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def456ghi')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def456ghi789'), 'abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def456ghi789')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def456ghi789abc'), 'abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def456ghi789abc')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123'), 'abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123')
        self.assertEqual(move_num('abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def'), 'abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def456ghi789abc123def')
        self.assertEqual(move_num('abc123def