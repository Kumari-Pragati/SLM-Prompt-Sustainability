import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(dig_let("a1b2c3"), (3, 3))
        self.assertEqual(dig_let("123abc"), (3, 3))
        self.assertEqual(dig_let("a1b2c3d4e5"), (5, 5))

    def test_edge_cases(self):
        self.assertEqual(dig_let(""), (0, 0))
        self.assertEqual(dig_let("1234567890"), (0, 10))
        self.assertEqual(dig_let("abcdefghijklmnopqrstuvwxyz"), (26, 0))
        self.assertEqual(dig_let("0123456789"), (0, 10))

    def test_corner_cases(self):
        self.assertEqual(dig_let("a1b2c3d4e5f6g7h8i9j0"), (10, 10))
        self.assertEqual(dig_let("1a2b3c4d5e6f7g8h9i0j"), (10, 10))
        self.assertEqual(dig_let("1234567890abcdefghijklmnopqrstuvwxyz"), (26, 10))

    def test_invalid_inputs(self):
        # The function does not handle invalid inputs explicitly.
        # So, we will check if it raises an exception.
        with self.assertRaises(TypeError):
            dig_let(123)
        with self.assertRaises(TypeError):
            dig_let(["a", "b", "c"])
        with self.assertRaises(TypeError):
            dig_let(None)
