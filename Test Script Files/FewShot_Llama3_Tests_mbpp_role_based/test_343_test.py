import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(dig_let("Hello123"), (4, 3))

    def test_empty_string(self):
        self.assertEqual(dig_let(""), (0, 0))

    def test_all_digits(self):
        self.assertEqual(dig_let("123456"), (0, 6))

    def test_all_letters(self):
        self.assertEqual(dig_let("abcdef"), (6, 0))

    def test_mixed_input(self):
        self.assertEqual(dig_let("Hello123abc"), (6, 3))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            dig_let(123)
