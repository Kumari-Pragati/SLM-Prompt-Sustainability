import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):

    def test_normal_case(self):
        self.assertTrue(is_allowed_specific_char("HelloWorld123."))
        self.assertTrue(is_allowed_specific_char("ABC_def456"))

    def test_edge_cases(self):
        self.assertTrue(is_allowed_specific_char(""))
        self.assertTrue(is_allowed_specific_char("a"))
        self.assertTrue(is_allowed_specific_char("z"))
        self.assertTrue(is_allowed_specific_char("0"))
        self.assertTrue(is_allowed_specific_char("9"))
        self.assertTrue(is_allowed_specific_char("."))
        self.assertTrue(is_allowed_specific_char(".."))
        self.assertTrue(is_allowed_specific_char("!_@#$%^&*()-+={}[]|;:,.<>?"))
        self.assertTrue(is_allowed_specific_char("!_@#$%^&*()-+={}[]|;:,.<>?" * 100))

    def test_boundary_cases(self):
        self.assertTrue(is_allowed_specific_char("Aa"))
        self.assertTrue(is_allowed_specific_char("Zz"))
        self.assertTrue(is_allowed_specific_char("01"))
        self.assertTrue(is_allowed_specific_char("98"))
        self.assertTrue(is_allowed_specific_char("..."))
        self.assertTrue(is_allowed_specific_char("_."))
        self.assertTrue(is_allowed_specific_char(".a"))
        self.assertTrue(is_allowed_specific_char("a."))
        self.assertTrue(is_allowed_specific_char("a.b"))
        self.assertTrue(is_allowed_specific_char("a.b."))
        self.assertTrue(is_allowed_specific_char("a.b.c"))
        self.assertTrue(is_allowed_specific_char("a.b.c."))
        self.assertTrue(is_allowed_specific_char("a.b.c.d"))
        self.assertTrue(is_allowed_specific_char("a.b.c.d."))

    def test_invalid_inputs(self):
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
        self.assertFalse(is_allowed_specific_char("{"))
        self.assertFalse(is_allowed_specific_char("}"))
        self.assertFalse(is_allowed_specific_char("["))
        self.assertFalse(is_allowed_specific_char("]"))
        self.assertFalse(is_allowed_specific_char("|"))
        self.assertFalse(is_allowed_specific_char(";"))
        self.assertFalse(is_allowed_specific_char(":"))
        self.assertFalse(is_allowed_specific_char(","))
        self.assertFalse(is_allowed_specific_char("<"))
        self.assertFalse(is_allowed_specific_char(">"))
        self.assertFalse(is_allowed_specific_char(" "))
        self.assertFalse(is_allowed_specific_char("\t"))
        self.assertFalse(is_allowed_specific_char("\n"))
        self.assertFalse(is_allowed_specific_char("\r"))
        self.assertFalse(is_allowed_specific_char("\f"))
        self.assertFalse(is_allowed_specific_