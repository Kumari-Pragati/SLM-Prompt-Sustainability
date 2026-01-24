import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(dig_let("abc123"), (3, 3))
        self.assertEqual(dig_let("123abc"), (1, 3))

    def test_edge_cases(self):
        self.assertEqual(dig_let(""), (0, 0))
        self.assertEqual(dig_let("0"), (0, 1))
        self.assertEqual(dig_let("z"), (1, 0))
        self.assertEqual(dig_let("1a"), (1, 1))
        self.assertEqual(dig_let("z123"), (1, 3))

    def test_complex_cases(self):
        self.assertEqual(dig_let("A1B2C3"), (3, 3))
        self.assertEqual(dig_let("1A2B3C"), (1, 3))
        self.assertEqual(dig_let("!@#$%^&*()_+-=abc123"), (10, 7))
        self.assertEqual(dig_let("abc123!@#$%^&*()_+-="), (3, 7))
