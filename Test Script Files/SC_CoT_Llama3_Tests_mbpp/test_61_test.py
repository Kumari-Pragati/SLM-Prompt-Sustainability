import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_Substrings("12345", 5), 1)

    def test_edge_case(self):
        self.assertEqual(count_Substrings("123", 3), 0)

    def test_edge_case2(self):
        self.assertEqual(count_Substrings("123456", 6), 1)

    def test_edge_case3(self):
        self.assertEqual(count_Substrings("123456789", 9), 1)

    def test_edge_case4(self):
        self.assertEqual(count_Substrings("1234567890", 10), 1)

    def test_edge_case5(self):
        self.assertEqual(count_Substrings("12345678901", 10), 1)

    def test_edge_case6(self):
        self.assertEqual(count_Substrings("123456789012", 12), 1)

    def test_edge_case7(self):
        self.assertEqual(count_Substrings("1234567890123", 12), 1)

    def test_edge_case8(self):
        self.assertEqual(count_Substrings("123456789012345", 12), 1)

    def test_edge_case9(self):
        self.assertEqual(count_Substrings("1234567890123456", 12), 1)

    def test_edge_case10(self):
        self.assertEqual(count_Substrings("123456789012345678", 12), 1)

    def test_edge_case11(self):
        self.assertEqual(count_Substrings("1234567890123456789", 12), 1)

    def test_edge_case12(self):
        self.assertEqual(count_Substrings("123456789012345678901", 12), 1)

    def test_edge_case13(self):
        self.assertEqual(count_Substrings("1234567890123456789012", 12), 1)

    def test_edge_case14(self):
        self.assertEqual(count_Substrings("123456789012345678901234", 12), 1)

    def test_edge_case15(self):
        self.assertEqual(count_Substrings("1234567890123456789012345", 12), 1)

    def test_edge_case16(self):
        self.assertEqual(count_Substrings("123456789012345678901234567", 12), 1)

    def test_edge_case17(self):
        self.assertEqual(count_Substrings("1234567890123456789012345678", 12), 1)

    def test_edge_case18(self):
        self.assertEqual(count_Substrings("12345678901234567890123456789", 12), 1)

    def test_edge_case19(self):
        self.assertEqual(count_Substrings("123456789012345678901234567890", 12), 1)

    def test_edge_case20(self):
        self.assertEqual(count_Substrings("1234567890123456789012345678901", 12), 1)

    def test_edge_case21(self):
        self.assertEqual(count_Substrings("12345678901234567890123456789012", 12), 1)

    def test_edge_case22(self):
        self.assertEqual(count_Substrings("123456789012345678901234567890123", 12), 1)

    def test_edge_case23(self):
        self.assertEqual(count_Substrings("1234567890123456789012345678901234", 12), 1)

    def test_edge_case24(self):
        self.assertEqual(count_Substrings("12345678901234567890123456789012345", 12), 1)

    def test_edge_case25(self):
        self.assertEqual(count_Substrings("123456789012345678901234567890123456", 12), 1)

    def test_edge_case26(self):
        self.assertEqual(count_Substrings("1234567890123456789012345678901234567", 12), 1)

    def test_edge_case27(self):
        self.assertEqual(count_Substrings("12345678901234567890123456789012345678", 12), 1)

    def test_edge_case28(self):
        self.assertEqual(count_Substrings("123456789012345678901234567890123456789", 12), 1)

    def test_edge_case29(self):
        self.assertEqual(count_Substrings("1234567890123456789012345678901234567890", 12), 1)

    def test_edge_case30(self):
        self.assertEqual(count_Substrings("12345678901234567890123456789012345678901", 12), 1)

    def test_edge_case31(self):
        self.assertEqual(count_Substrings("123456789012345678901234567890123456789012", 12), 1)

    def test_edge_case32(self):
        self.assertEqual(count_Substrings("1234567890123456789012345678901234567890123",