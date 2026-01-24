import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_extra_char("Hello World!"), "HelloWorld")

    def test_edge_case1(self):
        self.assertEqual(remove_extra_char("Hello_World!"), "HelloWorld")

    def test_edge_case2(self):
        self.assertEqual(remove_extra_char("Hello*World!"), "HelloWorld")

    def test_edge_case3(self):
        self.assertEqual(remove_extra_char("Hello-World!"), "HelloWorld")

    def test_edge_case4(self):
        self.assertEqual(remove_extra_char("Hello World!"), "HelloWorld")

    def test_edge_case5(self):
        self.assertEqual(remove_extra_char("Hello World123!"), "HelloWorld123")

    def test_edge_case6(self):
        self.assertEqual(remove_extra_char("Hello World!123"), "HelloWorld123")

    def test_edge_case7(self):
        self.assertEqual(remove_extra_char("Hello World!12345"), "HelloWorld12345")

    def test_edge_case8(self):
        self.assertEqual(remove_extra_char("Hello World!123456"), "HelloWorld123456")

    def test_edge_case9(self):
        self.assertEqual(remove_extra_char("Hello World!1234567"), "HelloWorld1234567")

    def test_edge_case10(self):
        self.assertEqual(remove_extra_char("Hello World!12345678"), "HelloWorld12345678")

    def test_edge_case11(self):
        self.assertEqual(remove_extra_char("Hello World!123456789"), "HelloWorld123456789")

    def test_edge_case12(self):
        self.assertEqual(remove_extra_char("Hello World!1234567890"), "HelloWorld1234567890")

    def test_edge_case13(self):
        self.assertEqual(remove_extra_char("Hello World!12345678901"), "HelloWorld12345678901")

    def test_edge_case14(self):
        self.assertEqual(remove_extra_char("Hello World!123456789012"), "HelloWorld123456789012")

    def test_edge_case15(self):
        self.assertEqual(remove_extra_char("Hello World!1234567890123"), "HelloWorld1234567890123")

    def test_edge_case16(self):
        self.assertEqual(remove_extra_char("Hello World!12345678901234"), "HelloWorld12345678901234")

    def test_edge_case17(self):
        self.assertEqual(remove_extra_char("Hello World!123456789012345"), "HelloWorld123456789012345")

    def test_edge_case18(self):
        self.assertEqual(remove_extra_char("Hello World!1234567890123456"), "HelloWorld1234567890123456")

    def test_edge_case19(self):
        self.assertEqual(remove_extra_char("Hello World!12345678901234567"), "HelloWorld12345678901234567")

    def test_edge_case20(self):
        self.assertEqual(remove_extra_char("Hello World!123456789012345678"), "HelloWorld123456789012345678")

    def test_edge_case21(self):
        self.assertEqual(remove_extra_char("Hello World!1234567890123456789"), "HelloWorld1234567890123456789")

    def test_edge_case22(self):
        self.assertEqual(remove_extra_char("Hello World!12345678901234567890"), "HelloWorld12345678901234567890")

    def test_edge_case23(self):
        self.assertEqual(remove_extra_char("Hello World!123456789012345678901"), "HelloWorld123456789012345678901")

    def test_edge_case24(self):
        self.assertEqual(remove_extra_char("Hello World!123456789012345678902"), "HelloWorld123456789012345678902")

    def test_edge_case25(self):
        self.assertEqual(remove_extra_char("Hello World!123456789012345678903"), "HelloWorld123456789012345678903")

    def test_edge_case26(self):
        self.assertEqual(remove_extra_char("Hello World!123456789012345678904"), "HelloWorld123456789012345678904")

    def test_edge_case27(self):
        self.assertEqual(remove_extra_char("Hello World!123456789012345678905"), "HelloWorld123456789012345678905")

    def test_edge_case28(self):
        self.assertEqual(remove_extra_char("Hello World!123456789012345678906"), "HelloWorld123456789012345678906")

    def test_edge_case29(self):
        self.assertEqual(remove_extra_char("Hello World!123456789012345678907"), "HelloWorld123456789012345678907")

    def test_edge_case30(self):
        self.assertEqual(remove_extra_char("Hello World!123456789012345678908"), "HelloWorld123456789012345678908")

    def test_edge_case31(self):
        self.assertEqual(remove_extra_char("Hello World!123456789012345678909"),