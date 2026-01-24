import unittest
from mbpp_321_code import find_demlo

class TestFindDemlo(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(find_demlo("abc"), "123456789abc987654321")

    def test_empty(self):
        self.assertEqual(find_demlo(""), "")

    def test_single_char(self):
        self.assertEqual(find_demlo("a"), "123a321")

    def test_multiple_chars(self):
        self.assertEqual(find_demlo("abc"), "123456789abc987654321")

    def test_long_string(self):
        self.assertEqual(find_demlo("abcdefghijklmnopqrstuvwxyz"), "123456789abcdefghijklmnopqrstuvwxyz987654321")

    def test_negative(self):
        with self.assertRaises(TypeError):
            find_demlo(-1)

    def test_non_string(self):
        with self.assertRaises(TypeError):
            find_demlo(123)
