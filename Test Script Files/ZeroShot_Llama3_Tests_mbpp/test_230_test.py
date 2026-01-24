import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):

    def test_replace_blank(self):
        self.assertEqual(replace_blank("Hello World", "*"), "Hello*World")
        self.assertEqual(replace_blank("Python is awesome", "_"), "Python_is_awesome")
        self.assertEqual(replace_blank("   Hello   World   ", "*"), "Hello*World")
        self.assertEqual(replace_blank("No blanks", "x"), "No blanks")
        self.assertEqual(replace_blank("", "x"), "")
