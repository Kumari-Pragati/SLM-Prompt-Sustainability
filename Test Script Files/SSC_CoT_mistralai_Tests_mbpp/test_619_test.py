import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(move_num("abc123def"), "abcdef123")
        self.assertEqual(move_num("1234567890"), "1234567890")
        self.assertEqual(move_num("0123456789"), "0123456789")

    def test_edge_cases(self):
        self.assertEqual(move_num(""), "")
        self.assertEqual(move_num(" "), "")
        self.assertEqual(move_num("a"), "a")
        self.assertEqual(move_num("1"), "1")
        self.assertEqual(move_num("1a"), "1a")
        self.assertEqual(move_num("z"), "z")
        self.assertEqual(move_num("z1"), "z1")
        self.assertEqual(move_num("1z"), "1z")

    def test_boundary_cases(self):
        self.assertEqual(move_num("012345678901"), "012345678901")
        self.assertEqual(move_num("123456789012"), "123456789012")
        self.assertEqual(move_num("1234567890123"), "1234567890123")
        self.assertEqual(move_num("12345678901234"), "12345678901234")
        self.assertEqual(move_num("123456789012345"), "123456789012345")
        self.assertEqual(move_num("1234567890123456"), "1234567890123456")
        self.assertEqual(move_num("12345678901234567"), "12345678901234567")
        self.assertEqual(move_num("123456789012345678"), "123456789012345678")
        self.assertEqual(move_num("1234567890123456789"), "1234567890123456789")
