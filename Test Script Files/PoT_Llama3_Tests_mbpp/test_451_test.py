import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_whitespaces("Hello World"), "HelloWorld")

    def test_edge_case(self):
        self.assertEqual(remove_whitespaces("   Hello   World   "), "HelloWorld")

    def test_edge_case2(self):
        self.assertEqual(remove_whitespaces("Hello\nWorld"), "HelloWorld")

    def test_edge_case3(self):
        self.assertEqual(remove_whitespaces("Hello\tWorld"), "HelloWorld")

    def test_edge_case4(self):
        self.assertEqual(remove_whitespaces("Hello\rWorld"), "HelloWorld")

    def test_edge_case5(self):
        self.assertEqual(remove_whitespaces("Hello\r\nWorld"), "HelloWorld")

    def test_edge_case6(self):
        self.assertEqual(remove_whitespaces("Hello   World   \n"), "HelloWorld")

    def test_edge_case7(self):
        self.assertEqual(remove_whitespaces("Hello   World   \t"), "HelloWorld")

    def test_edge_case8(self):
        self.assertEqual(remove_whitespaces("Hello   World   \r"), "HelloWorld")

    def test_edge_case9(self):
        self.assertEqual(remove_whitespaces("Hello   World   \r\n"), "HelloWorld")

    def test_edge_case10(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \n"), "HelloWorld")

    def test_edge_case11(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \t"), "HelloWorld")

    def test_edge_case12(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \r"), "HelloWorld")

    def test_edge_case13(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \r\n"), "HelloWorld")

    def test_edge_case14(self):
        self.assertEqual(remove_whitespaces("Hello   World   \n   "), "HelloWorld")

    def test_edge_case15(self):
        self.assertEqual(remove_whitespaces("Hello   World   \t   "), "HelloWorld")

    def test_edge_case16(self):
        self.assertEqual(remove_whitespaces("Hello   World   \r   "), "HelloWorld")

    def test_edge_case17(self):
        self.assertEqual(remove_whitespaces("Hello   World   \r\n   "), "HelloWorld")

    def test_edge_case18(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \n   "), "HelloWorld")

    def test_edge_case19(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \t   "), "HelloWorld")

    def test_edge_case20(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \r   "), "HelloWorld")

    def test_edge_case21(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \r\n   "), "HelloWorld")

    def test_edge_case22(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \n   \t   "), "HelloWorld")

    def test_edge_case23(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \n   \r   "), "HelloWorld")

    def test_edge_case24(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \n   \r\n   "), "HelloWorld")

    def test_edge_case25(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \t   \n   "), "HelloWorld")

    def test_edge_case26(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \t   \r   "), "HelloWorld")

    def test_edge_case27(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \t   \r\n   "), "HelloWorld")

    def test_edge_case28(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \r   \n   "), "HelloWorld")

    def test_edge_case29(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \r   \t   "), "HelloWorld")

    def test_edge_case30(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \r   \r\n   "), "HelloWorld")

    def test_edge_case31(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \r   \t   \n   "), "HelloWorld")

    def test_edge_case32(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \r   \t   \r   "), "HelloWorld")

    def test_edge_case33(self):
        self.assertEqual(remove_whitespaces("   Hello   World   \r   \t   \r\n   "), "HelloWorld")

    def test_edge_case34(self):