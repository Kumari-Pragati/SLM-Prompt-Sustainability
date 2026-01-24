import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Swaps('abc', 'abc'), 0)

    def test_edge_case1(self):
        self.assertEqual(min_Swaps('abc', 'abd'), 1)

    def test_edge_case2(self):
        self.assertEqual(min_Swaps('abc', 'bca'), 1)

    def test_edge_case3(self):
        self.assertEqual(min_Swaps('abc', 'abcd'), 1)

    def test_edge_case4(self):
        self.assertEqual(min_Swaps('abc', 'def'), 2)

    def test_edge_case5(self):
        self.assertEqual(min_Swaps('abc', 'defgh'), 3)

    def test_edge_case6(self):
        self.assertEqual(min_Swaps('abc', 'defghij'), 4)

    def test_edge_case7(self):
        self.assertEqual(min_Swaps('abc', 'defghijkl'), 5)

    def test_edge_case8(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmn'), 6)

    def test_edge_case9(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmno'), 7)

    def test_edge_case10(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnop'), 8)

    def test_edge_case11(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopq'), 9)

    def test_edge_case12(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqr'), 10)

    def test_edge_case13(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrs'), 11)

    def test_edge_case14(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrst'), 12)

    def test_edge_case15(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstu'), 13)

    def test_edge_case16(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuv'), 14)

    def test_edge_case17(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuva'), 15)

    def test_edge_case18(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvw'), 16)

    def test_edge_case19(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvaab'), 17)

    def test_edge_case20(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvwxyz'), 18)

    def test_edge_case21(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvaabbc'), 19)

    def test_edge_case22(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvwxyza'), 20)

    def test_edge_case23(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvaabbcde'), 21)

    def test_edge_case24(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvwxyzabc'), 22)

    def test_edge_case25(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvaabbcdef'), 23)

    def test_edge_case26(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvwxyzabcd'), 24)

    def test_edge_case27(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvaabbcdefgh'), 25)

    def test_edge_case28(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvwxyzabcdgh'), 26)

    def test_edge_case29(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvaabbcdefghi'), 27)

    def test_edge_case30(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvwxyzabcdghij'), 28)

    def test_edge_case31(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvaabbcdefghij'), 29)

    def test_edge_case32(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvwxyzabcdghijk'), 30)

    def test_edge_case33(self):
        self.assertEqual(min_Swaps('abc', 'defghijklmnopqrstuvaabbcdefghijk'),