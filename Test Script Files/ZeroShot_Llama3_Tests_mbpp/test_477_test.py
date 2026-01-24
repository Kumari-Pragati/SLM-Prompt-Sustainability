import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):

    def test_lower(self):
        self.assertTrue(is_lower("hello"))
        self.assertTrue(is_lower("world"))
        self.assertTrue(is_lower("python"))
        self.assertTrue(is_lower("unittest"))

    def test_upper(self):
        self.assertFalse(is_lower("HELLO"))
        self.assertFalse(is_lower("WORLD"))
        self.assertFalse(is_lower("PYTHON"))
        self.assertFalse(is_lower("UNittest"))

    def test_mixed(self):
        self.assertTrue(is_lower("HeLlO"))
        self.assertTrue(is_lower("WoRlD"))
        self.assertTrue(is_lower("PyThOn"))
        self.assertTrue(is_lower("UnItEsT"))

    def test_empty(self):
        self.assertTrue(is_lower(""))

    def test_non_string(self):
        with self.assertRaises(TypeError):
            is_lower(123)
