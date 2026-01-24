import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):
    def test_typical(self):
        self.assertTrue(is_upper('UPPER'))
        self.assertTrue(is_upper('UPPERCASE'))
        self.assertTrue(is_upper('ALLCAPS'))

    def test_edge(self):
        self.assertTrue(is_upper('lower'))
        self.assertTrue(is_upper('mixedCase'))
        self.assertTrue(is_upper('ALLlower'))

    def test_boundary(self):
        self.assertTrue(is_upper(''))
        self.assertTrue(is_upper('UPPERCASE '))

    def test_invalid(self):
        with self.assertRaises(TypeError):
            is_upper(123)
        with self.assertRaises(TypeError):
            is_upper(None)
