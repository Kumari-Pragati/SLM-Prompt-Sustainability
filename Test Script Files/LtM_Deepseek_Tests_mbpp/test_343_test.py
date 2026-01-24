import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(dig_let("abc123"), (3, 3))
        self.assertEqual(dig_let("123abc"), (3, 3))
        self.assertEqual(dig_let("123456"), (0, 6))
        self.assertEqual(dig_let("abcdef"), (6, 0))

    def test_edge_conditions(self):
        self.assertEqual(dig_let(""), (0, 0))
        self.assertEqual(dig_let("1234567890"), (0, 10))
        self.assertEqual(dig_let("abcdefghijklmnopqrstuvwxyz"), (26, 0))
        self.assertEqual(dig_let("0123456789"), (0, 10))

    def test_complex_cases(self):
        self.assertEqual(dig_let("a1b2c3d4e5f6"), (6, 6))
        self.assertEqual(dig_let("1a2b3c4d5e6f7g8h9i0j"), (10, 10))
        self.assertEqual(dig_let("1234567890abcdefghijklmnopqrstuvwxyz"), (26, 10))
        self.assertEqual(dig_let("abcdefghijklmnopqrstuvwxyz1234567890"), (26, 10))
