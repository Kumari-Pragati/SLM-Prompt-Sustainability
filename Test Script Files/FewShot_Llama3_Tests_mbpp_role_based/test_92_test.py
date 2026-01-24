import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):
    def test_undulating_string(self):
        self.assertTrue(is_undulating("ababab"))

    def test_non_undulating_string(self):
        self.assertFalse(is_undulating("abc"))

    def test_string_with_length_2(self):
        self.assertFalse(is_undulating("aa"))

    def test_string_with_length_3(self):
        self.assertFalse(is_undulating("aba"))

    def test_string_with_length_4(self):
        self.assertTrue(is_undulating("abab"))

    def test_string_with_length_5(self):
        self.assertFalse(is_undulating("ababc"))
