import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_allowed_specific_char("abc123.def"))
        self.assertTrue(is_allowed_specific_char("ABC_123.DEF"))
        self.assertTrue(is_allowed_specific_char("abc.123"))
        self.assertTrue(is_allowed_specific_char("ABC_123"))

    def test_edge_case(self):
        self.assertTrue(is_allowed_specific_char("aBc123.dEf"))
        self.assertTrue(is_allowed_specific_char("aBc_123.dEf"))
        self.assertTrue(is_allowed_specific_char("aBc123-dEf"))
        self.assertTrue(is_allowed_specific_char("aBc123_dEf"))
        self.assertTrue(is_allowed_specific_char("aBc123.dEf_"))
        self.assertTrue(is_allowed_specific_char("aBc123-dEf_"))

    def test_boundary_case(self):
        self.assertTrue(is_allowed_specific_char("a"))
        self.assertTrue(is_allowed_specific_char("A"))
        self.assertTrue(is_allowed_specific_char("1"))
        self.assertTrue(is_allowed_specific_char("."))
        self.assertTrue(is_allowed_specific_char(""))
