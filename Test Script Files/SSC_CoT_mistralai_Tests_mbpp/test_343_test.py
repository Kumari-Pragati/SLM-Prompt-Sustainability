import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(dig_let('abc123'), (3, 3))
        self.assertEqual(dig_let('123abc'), (1, 3))
        self.assertEqual(dig_let('1234567890'), (0, 10))

    def test_edge_input(self):
        self.assertEqual(dig_let(''), (0, 0))
        self.assertEqual(dig_let('0'), (0, 1))
        self.assertEqual(dig_let('12345678901'), (1, 10))
        self.assertEqual(dig_let('abcdefghijklmnopqrstuvwxyz'), (26, 0))
        self.assertEqual(dig_let('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), (26, 0))
        self.assertEqual(dig_let('!@#$%^&*()_+-=[]{};:'\'<>,.?/'), (0, 0))

    def test_special_input(self):
        self.assertEqual(dig_let('1a2b3c'), (3, 3))
        self.assertEqual(dig_let('1_2_3_4'), (4, 4))
        self.assertEqual(dig_let('1_2_3_4_5'), (5, 4))
        self.assertEqual(dig_let('1_2_3_4_5_6_7_8_9_0'), (10, 10))
