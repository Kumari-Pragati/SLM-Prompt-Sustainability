import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Swaps('abc', 'abc'), 0)

    def test_edge_case1(self):
        self.assertEqual(min_Swaps('abc', 'abcd'), 1)

    def test_edge_case2(self):
        self.assertEqual(min_Swaps('abc', 'abcdx'), 2)

    def test_edge_case3(self):
        self.assertEqual(min_Swaps('abc', 'abcdxy'), 2)

    def test_edge_case4(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyz'), 2)

    def test_edge_case5(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabc'), 2)

    def test_edge_case6(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcd'), 2)

    def test_edge_case7(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabc'), 2)

    def test_edge_case8(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabc'), 2)

    def test_edge_case9(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabc'), 2)

    def test_edge_case10(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabc'), 2)

    def test_edge_case11(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabc'), 2)

    def test_edge_case12(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabc'), 2)

    def test_edge_case13(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabc'), 2)

    def test_edge_case14(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabcabc'), 2)

    def test_edge_case15(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabcabcabc'), 2)

    def test_edge_case16(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabcabcabcabc'), 2)

    def test_edge_case17(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabcabcabcabcabc'), 2)

    def test_edge_case18(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabcabcabcabcabcabc'), 2)

    def test_edge_case19(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabcabcabcabcabcabcabc'), 2)

    def test_edge_case20(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabcabcabcabcabcabcabcabc'), 2)

    def test_edge_case21(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'), 2)

    def test_edge_case22(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'), 2)

    def test_edge_case23(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'), 2)

    def test_edge_case24(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'), 2)

    def test_edge_case25(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'), 2)

    def test_edge_case26(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'), 2)

    def test_edge_case27(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'), 2)

    def test_edge_case28(self):
        self.assertEqual(min_Swaps('abc', 'abcdxyzabcdabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'), 2)

    def test