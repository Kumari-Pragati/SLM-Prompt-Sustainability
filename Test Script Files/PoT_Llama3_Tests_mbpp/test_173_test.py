import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSplchar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_splchar("Hello, World!"), "Hello World")

    def test_edge_case(self):
        self.assertEqual(remove_splchar("Hello_World"), "Hello World")

    def test_edge_case2(self):
        self.assertEqual(remove_splchar("Hello World!"), "Hello World")

    def test_edge_case3(self):
        self.assertEqual(remove_splchar("Hello"), "Hello")

    def test_edge_case4(self):
        self.assertEqual(remove_splchar("12345"), "12345")

    def test_edge_case5(self):
        self.assertEqual(remove_splchar("a b c"), "abc")

    def test_edge_case6(self):
        self.assertEqual(remove_splchar("a_b_c"), "abc")

    def test_edge_case7(self):
        self.assertEqual(remove_splchar("a b c d"), "abcd")

    def test_edge_case8(self):
        self.assertEqual(remove_splchar("a_b_c_d"), "abcd")

    def test_edge_case9(self):
        self.assertEqual(remove_splchar("a b c d e"), "abcde")

    def test_edge_case10(self):
        self.assertEqual(remove_splchar("a_b_c_d_e"), "abcde")

    def test_edge_case11(self):
        self.assertEqual(remove_splchar("a b c d e f"), "abcdef")

    def test_edge_case12(self):
        self.assertEqual(remove_splchar("a_b_c_d_e_f"), "abcdef")

    def test_edge_case13(self):
        self.assertEqual(remove_splchar("a b c d e f g"), "abcdefg")

    def test_edge_case14(self):
        self.assertEqual(remove_splchar("a_b_c_d_e_f_g"), "abcdefg")

    def test_edge_case15(self):
        self.assertEqual(remove_splchar("a b c d e f g h"), "abcdefgh")

    def test_edge_case16(self):
        self.assertEqual(remove_splchar("a_b_c_d_e_f_g_h"), "abcdefgh")

    def test_edge_case17(self):
        self.assertEqual(remove_splchar("a b c d e f g h i"), "abcdefghi")

    def test_edge_case18(self):
        self.assertEqual(remove_splchar("a_b_c_d_e_f_g_h_i"), "abcdefghi")

    def test_edge_case19(self):
        self.assertEqual(remove_splchar("a b c d e f g h i j"), "abcdefghij")

    def test_edge_case20(self):
        self.assertEqual(remove_splchar("a_b_c_d_e_f_g_h_i_j"), "abcdefghij")
