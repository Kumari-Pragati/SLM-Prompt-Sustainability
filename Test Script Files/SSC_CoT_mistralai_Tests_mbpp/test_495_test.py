import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(remove_lowercase("HelloWorld"), "HELLOWORLD")

    def test_edge_cases(self):
        self.assertEqual(remove_lowercase(""), "")
        self.assertEqual(remove_lowercase("A"), "A")
        self.assertEqual(remove_lowercase("Aa"), "A")
        self.assertEqual(remove_lowercase("Z"), "Z")
        self.assertEqual(remove_lowercase("Zz"), "Z")

    def test_boundary_conditions(self):
        self.assertEqual(remove_lowercase("AaBbCc"), "AaBbCc")
        self.assertEqual(remove_lowercase("AaBbCcDd"), "AaBbCcDd")
        self.assertEqual(remove_lowercase("AaBbCcDdEe"), "AaBbCcDdEe")

    def test_special_cases(self):
        self.assertEqual(remove_lowercase("123"), "123")
        self.assertEqual(remove_lowercase("_"), "_")
        self.assertEqual(remove_lowercase("_123"), "_123")
        self.assertEqual(remove_lowercase("123_"), "123_")
        self.assertEqual(remove_lowercase("123_456"), "123_456")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_lowercase(123)
        with self.assertRaises(TypeError):
            remove_lowercase(None)
