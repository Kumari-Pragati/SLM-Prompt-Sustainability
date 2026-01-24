import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):

    def test_remove_whitespaces(self):
        self.assertEqual(remove_whitespaces("Hello   World!"), "HelloWorld!")
        self.assertEqual(remove_whitespaces("   This   is   a   test   "), "Thisisatest")
        self.assertEqual(remove_whitespaces("   "), "")
        self.assertEqual(remove_whitespaces("   Hello   World!   "), "HelloWorld!")
        self.assertEqual(remove_whitespaces("   Hello   World!   with   multiple   spaces   "), "HelloWorld!withmultiple spaces")
        self.assertEqual(remove_whitespaces("   Hello   World!   with   multiple   spaces   and   tabs   "), "HelloWorld!withmultiple spacesand\tabs")

    def test_remove_whitespaces_with_tabs(self):
        self.assertEqual(remove_whitespaces("Hello\tWorld!"), "HelloWorld!")
        self.assertEqual(remove_whitespaces("   This\tis\ta\ttest\t"), "Thisisatest")
        self.assertEqual(remove_whitespaces("   \t"), "")
        self.assertEqual(remove_whitespaces("   Hello\tWorld!   "), "HelloWorld!")
        self.assertEqual(remove_whitespaces("   Hello\tWorld!   with\tmultiple\tspaces\t"), "HelloWorld!withmultiple spaces")
        self.assertEqual(remove_whitespaces("   Hello\tWorld!   with\tmultiple\tspaces\tand\ttabs\t"), "HelloWorld!withmultiple spacesand\ttabs")
