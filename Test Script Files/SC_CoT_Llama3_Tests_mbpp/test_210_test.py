import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(is_allowed_specific_char("HelloWorld."))
        self.assertTrue(is_allowed_specific_char("Hello123."))
        self.assertTrue(is_allowed_specific_char("HelloWorld123."))

    def test_edge_case(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld!"))
        self.assertFalse(is_allowed_specific_char("Hello123!"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123!"))

    def test_edge_case2(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld@"))
        self.assertFalse(is_allowed_specific_char("Hello123@"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123@"))

    def test_edge_case3(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld#"))
        self.assertFalse(is_allowed_specific_char("Hello123#"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123#"))

    def test_edge_case4(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld$"))
        self.assertFalse(is_allowed_specific_char("Hello123$"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123$"))

    def test_edge_case5(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld%"))
        self.assertFalse(is_allowed_specific_char("Hello123%"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123%"))

    def test_edge_case6(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld^"))
        self.assertFalse(is_allowed_specific_char("Hello123^"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123^"))

    def test_edge_case7(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld&"))
        self.assertFalse(is_allowed_specific_char("Hello123&"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123&"))

    def test_edge_case8(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld*"))
        self.assertFalse(is_allowed_specific_char("Hello123*"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123*"))

    def test_edge_case9(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld("))
        self.assertFalse(is_allowed_specific_char("Hello123("))
        self.assertFalse(is_allowed_specific_char("HelloWorld123("))

    def test_edge_case10(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld)"))
        self.assertFalse(is_allowed_specific_char("Hello123)"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123)"))

    def test_edge_case11(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld["))
        self.assertFalse(is_allowed_specific_char("Hello123["))
        self.assertFalse(is_allowed_specific_char("HelloWorld123["))

    def test_edge_case12(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld]"))
        self.assertFalse(is_allowed_specific_char("Hello123]"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123]"))

    def test_edge_case13(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld{"))
        self.assertFalse(is_allowed_specific_char("Hello123{"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123{"))

    def test_edge_case14(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld}"))
        self.assertFalse(is_allowed_specific_char("Hello123}"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123}"))

    def test_edge_case15(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld<"))
        self.assertFalse(is_allowed_specific_char("Hello123<"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123<"))

    def test_edge_case16(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld>"))
        self.assertFalse(is_allowed_specific_char("Hello123>"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123>"))

    def test_edge_case17(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld/"))
        self.assertFalse(is_allowed_specific_char("Hello123/"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123/"))

    def test_edge_case18(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld\\"))
        self.assertFalse(is_allowed_specific_char("Hello123\\"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123\\"))

    def test_edge_case19(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld|"))
        self.assertFalse(is_allowed_specific_char("Hello123|"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123|"))

    def test_edge_case20(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld~"))
        self.assertFalse(is_allowed_specific_char("Hello123~"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123~"))

    def test_edge_case21(self):
        self.assertFalse(is_allowed_specific_char("HelloWorld`"))
        self.assertFalse(is_allowed_specific_char("Hello123`"))
        self.assertFalse(is_allowed_specific_char("HelloWorld123`"))

    def test_edge_case22(self):
        self.assertFalse(is_allowed