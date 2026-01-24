import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_remove_lowercase_typical(self):
        self.assertEqual(remove_lowercase("Hello World"), "HW")

    def test_remove_lowercase_edge(self):
        self.assertEqual(remove_lowercase("123456"), "123456")

    def test_remove_lowercase_edge2(self):
        self.assertEqual(remove_lowercase("ABCDEF"), "ABCDEF")

    def test_remove_lowercase_edge3(self):
        self.assertEqual(remove_lowercase("abcdef"), "")

    def test_remove_lowercase_edge4(self):
        self.assertEqual(remove_lowercase("aAbBcCdDeEf"), "")

    def test_remove_lowercase_edge5(self):
        self.assertEqual(remove_lowercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def test_remove_lowercase_edge6(self):
        self.assertEqual(remove_lowercase("abcdefghijklmnopqrstuvwxyz"), "")

    def test_remove_lowercase_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_lowercase(123)

    def test_remove_lowercase_invalid_input2(self):
        with self.assertRaises(TypeError):
            remove_lowercase(None)
