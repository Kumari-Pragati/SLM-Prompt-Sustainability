import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):
    def test_simple_string(self):
        self.assertTrue(is_allowed_specific_char("abc123.def"))
        self.assertTrue(is_allowed_specific_char("ABC_123.DEF"))

    def test_edge_cases(self):
        self.assertTrue(is_allowed_specific_char("a"))
        self.assertTrue(is_allowed_specific_char("z"))
        self.assertTrue(is_allowed_specific_char("0"))
        self.assertTrue(is_allowed_specific_char("9"))
        self.assertTrue(is_allowed_specific_char("."))
        self.assertTrue(is_allowed_specific_char("_"))

        self.assertFalse(is_allowed_specific_char(""))
        self.assertFalse(is_allowed_specific_char(None))
        self.assertFalse(is_allowed_specific_char("!"))
        self.assertFalse(is_allowed_specific_char("@"))
        self.assertFalse(is_allowed_specific_char("#"))
        self.assertFalse(is_allowed_specific_char("%"))
        self.assertFalse(is_allowed_specific_char("^"))
        self.assertFalse(is_allowed_specific_char("&"))
        self.assertFalse(is_allowed_specific_char("*"))
        self.assertFalse(is_allowed_specific_char("("))
        self.assertFalse(is_allowed_specific_char(")"))
        self.assertFalse(is_allowed_specific_char("-"))
        self.assertFalse(is_allowed_specific_char("+"))
        self.assertFalse(is_allowed_specific_char("="))
        self.assertFalse(is_allowed_specific_char("{"))
        self.assertFalse(is_allowed_specific_char("}"))
        self.assertFalse(is_allowed_specific_char("["))
        self.assertFalse(is_allowed_specific_char("]"))
        self.assertFalse(is_allowed_specific_char("|"))
        self.assertFalse(is_allowed_specific_char("~"))
        self.assertFalse(is_allowed_specific_char("`"))
        self.assertFalse(is_allowed_specific_char(":"))
        self.assertFalse(is_allowed_specific_char(";"))
        self.assertFalse(is_allowed_specific_char("'"))
        self.assertFalse(is_allowed_specific_char('"'))
        self.assertFalse(is_allowed_specific_char(" "))
        self.assertFalse(is_allowed_specific_char("\t"))

    def test_complex_cases(self):
        self.assertTrue(is_allowed_specific_char("abc123.def.ghi"))
        self.assertTrue(is_allowed_specific_char("ABC_123.DEF_GHI"))
        self.assertTrue(is_allowed_specific_char("abc123.def.ghi.ijk"))
        self.assertTrue(is_allowed_specific_char("ABC_123.DEF_GHI_JKL"))
        self.assertTrue(is_allowed_specific_char("abc123.def.ghi.ijk.lmn"))
        self.assertTrue(is_allowed_specific_char("ABC_123.DEF_GHI_JKL_MNO"))
