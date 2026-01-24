import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):

    def test_upper(self):
        self.assertTrue(is_upper("UPPER"))
        self.assertTrue(is_upper("UPPERCASE"))
        self.assertTrue(is_upper("ALLCAPS"))

    def test_lower(self):
        self.assertFalse(is_upper("lower"))
        self.assertFalse(is_upper("lowercase"))
        self.assertFalse(is_upper("allcaps"))

    def test_mixed(self):
        self.assertFalse(is_upper("mixed"))
        self.assertFalse(is_upper("mixedcase"))
        self.assertFalse(is_upper("mixofcapsandlower"))

    def test_empty(self):
        self.assertFalse(is_upper(""))

    def test_non_string(self):
        with self.assertRaises(TypeError):
            is_upper(123)
