import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):
    def test_typical_use_cases(self):
        self.assertTrue(is_allowed_specific_char("abc123.def"))
        self.assertTrue(is_allowed_specific_char(""))

    def test_edge_conditions(self):
        self.assertTrue(is_allowed_specific_char("a"))
        self.assertTrue(is_allowed_specific_char("1"))
        self.assertTrue(is_allowed_specific_char("."))

    def test_boundary_conditions(self):
        self.assertTrue(is_allowed_specific_char("a"*210))
        self.assertFalse(is_allowed_specific_char("a"*211))

    def test_invalid_inputs(self):
        self.assertFalse(is_allowed_specific_char("a"*211))
        self.assertFalse(is_allowed_specific_char("!"))
        self.assertFalse(is_allowed_specific_char("@"))
        self.assertFalse(is_allowed_specific_char("#"))
        self.assertFalse(is_allowed_specific_char("$"))
        self.assertFalse(is_allowed_specific_char("%"))
        self.assertFalse(is_allowed_specific_char("^"))
        self.assertFalse(is_allowed_specific_char("&"))
        self.assertFalse(is_allowed_specific_char("*"))
        self.assertFalse(is_allowed_specific_char("("))
        self.assertFalse(is_allowed_specific_char(")"))
        self.assertFalse(is_allowed_specific_char("-"))
        self.assertFalse(is_allowed_specific_char("_"))
        self.assertFalse(is_allowed_specific_char("+"))
        self.assertFalse(is_allowed_specific_char("="))
        self.assertFalse(is_allowed_specific_char("{"))
        self.assertFalse(is_allowed_specific_char("}"))
        self.assertFalse(is_allowed_specific_char("[")
        self.assertFalse(is_allowed_specific_char("]"))
        self.assertFalse(is_allowed_specific_char(";"))
        self.assertFalse(is_allowed_specific_char(":"))
        self.assertFalse(is_allowed_specific_char("<"))
        self.assertFalse(is_allowed_specific_char(">"))
        self.assertFalse(is_allowed_specific_char("?"))
        self.assertFalse(is_allowed_specific_char("/"))
        self.assertFalse(is_allowed_specific_char("\\"))
        self.assertFalse(is_allowed_specific_char("|"))
        self.assertFalse(is_allowed_specific_char("~"))
        self.assertFalse(is_allowed_specific_char("`"))
