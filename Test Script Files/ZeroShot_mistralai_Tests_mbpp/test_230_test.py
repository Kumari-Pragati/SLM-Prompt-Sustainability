import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):

    def test_replace_blank_with_single_char(self):
        self.assertEqual(replace_blank("Hello World", "_"), "Hello_World")
        self.assertEqual(replace_blank("This is a test", "_"), "This_is_a_test")
        self.assertEqual(replace_blank("", "_"), "")

    def test_replace_blank_with_multiple_chars(self):
        self.assertEqual(replace_blank("Hello World", "X_Y"), "HelloX_YWorld")
        self.assertEqual(replace_blank("This is a test", "X_Y_Z"), "ThisX_Y_ZisX_Y_ZaX_Y_Ztest")
        self.assertEqual(replace_blank("", "X_Y"), "")

    def test_replace_blank_with_empty_char(self):
        self.assertEqual(replace_blank("Hello World", ""), "Hello   World")
        self.assertEqual(replace_blank("This is a test", ""), "This is a test")
        self.assertEqual(replace_blank("", ""), "")
