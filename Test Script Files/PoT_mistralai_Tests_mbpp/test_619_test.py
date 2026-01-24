import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(move_num("A1B2C3D4"), "A1BC2D3T4")
        self.assertEqual(move_num("1234567890"), "1234567890")
        self.assertEqual(move_num("abc123"), "abc123")

    def test_edge_case(self):
        self.assertEqual(move_num(""), "")
        self.assertEqual(move_num(" "), "")
        self.assertEqual(move_num("0"), "0")
        self.assertEqual(move_num("1"), "1")
        self.assertEqual(move_num("9"), "9")
        self.assertEqual(move_num("10"), "10")
        self.assertEqual(move_num("12345678901"), "12345678901")

    def test_corner_case(self):
        self.assertEqual(move_num("1a2b3c"), "1a2b3c")
        self.assertEqual(move_num("1_2_3_"), "1_2_3_")
        self.assertEqual(move_num("1-2-3-"), "1-2-3-")
        self.assertEqual(move_num("1A2B3C"), "1A2B3C")
        self.assertEqual(move_num("1_2_3_a"), "1_2_3_a")
        self.assertEqual(move_num("1-2-3-A"), "1-2-3-A")
