import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(max_run_uppercase("HelloWorld"), 1)

    def test_edge_case(self):
        self.assertEqual(max_run_uppercase("HelloWorld123"), 1)

    def test_edge_case2(self):
        self.assertEqual(max_run_uppercase("Hello123World"), 2)

    def test_edge_case3(self):
        self.assertEqual(max_run_uppercase("Hello123456"), 1)

    def test_edge_case4(self):
        self.assertEqual(max_run_uppercase("Hello123456789"), 1)

    def test_edge_case5(self):
        self.assertEqual(max_run_uppercase("Hello1234567890"), 1)

    def test_edge_case6(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABC"), 1)

    def test_edge_case7(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEF"), 1)

    def test_edge_case8(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFgh"), 1)

    def test_edge_case9(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghij"), 1)

    def test_edge_case10(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijkl"), 1)

    def test_edge_case11(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmn"), 1)

    def test_edge_case12(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmno"), 1)

    def test_edge_case13(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnop"), 1)

    def test_edge_case14(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopq"), 1)

    def test_edge_case15(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqr"), 1)

    def test_edge_case16(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqrt"), 1)

    def test_edge_case17(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqrstu"), 1)

    def test_edge_case18(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqrstuuv"), 1)

    def test_edge_case19(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqrstuuvwx"), 1)

    def test_edge_case20(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqrstuuvwxxy"), 1)

    def test_edge_case21(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqrstuuvwxxyyz"), 1)

    def test_edge_case22(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqrstuuvwxxyyzabc"), 1)

    def test_edge_case23(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqrstuuvwxxyyzabcd"), 1)

    def test_edge_case24(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqrstuuvwxxyyzabcdEf"), 1)

    def test_edge_case25(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqrstuuvwxxyyzabcdEfgh"), 1)

    def test_edge_case26(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqrstuuvwxxyyzabcdEfghi"), 1)

    def test_edge_case27(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqrstuuvwxxyyzabcdEfghij"), 1)

    def test_edge_case28(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqrstuuvwxxyyzabcdEfghijk"), 1)

    def test_edge_case29(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqrstuuvwxxyyzabcdEfghijkl"), 1)

    def test_edge_case30(self):
        self.assertEqual(max_run_uppercase("Hello1234567890ABCDEFghijklmnopqrstuuvwxxyyzabcdEfghijklm"), 1)

    def test_edge_case31(self):
        self.assertEqual(max_run_uppercase("Hello123