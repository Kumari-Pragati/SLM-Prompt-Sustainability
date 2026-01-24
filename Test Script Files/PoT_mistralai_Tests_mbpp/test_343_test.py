import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(dig_let("abc123"), (3, 3))
        self.assertEqual(dig_let("123abc"), (1, 3))
        self.assertEqual(dig_let("123456789"), (0, 9))
        self.assertEqual(dig_let("aBc123"), (3, 1))
        self.assertEqual(dig_let("123Abc"), (1, 3))

    def test_edge_cases(self):
        self.assertEqual(dig_let(""), (0, 0))
        self.assertEqual(dig_let("0"), (0, 1))
        self.assertEqual(dig_let("a"), (1, 0))
        self.assertEqual(dig_let("1"), (0, 1))
        self.assertEqual(dig_let("1234567890"), (0, 10))
        self.assertEqual(dig_let("abcdefghijklmnopqrstuvwxyz"), (26, 0))
        self.assertEqual(dig_let("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), (26, 0))
        self.assertEqual(dig_let("!@#$%^&*()_+-=[]{}|;:'\",.<>?/"), (0, 0)
