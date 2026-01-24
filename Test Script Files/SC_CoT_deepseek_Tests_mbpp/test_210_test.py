import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_allowed_specific_char("abc123.def"))
        self.assertTrue(is_allowed_specific_char(""))

    def test_edge_cases(self):
        self.assertTrue(is_allowed_specific_char("a"))
        self.assertTrue(is_allowed_specific_char("1"))
        self.assertTrue(is_allowed_specific_char("."))

    def test_boundary_cases(self):
        self.assertTrue(is_allowed_specific_char("a"*256))
        self.assertTrue(is_allowed_specific_char("1"*256))
        self.assertTrue(is_allowed_specific_char("."*256))

    def test_special_cases(self):
        self.assertFalse(is_allowed_specific_char("aBc123.deF!"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF@"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF#"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF$"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF%"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF^"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF&"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF*"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF("))
        self.assertFalse(is_allowed_specific_char("aBc123.deF)"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF-"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF_"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF+"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF="))
        self.assertFalse(is_allowed_specific_char("aBc123.deF{"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF}"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF|"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF\\"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF:"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF;"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF<"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF>"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF?"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF/"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF\\"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF'"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF\""))
        self.assertFalse(is_allowed_specific_char("aBc123.deF`"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF~"))
        self.assertFalse(is_allowed_specific_char("aBc123.deF["))
        self.assertFalse(is_allowed_specific_char("aBc123.deF]"))
        self.assertFalse(is_allowed_specific_char("aBc123