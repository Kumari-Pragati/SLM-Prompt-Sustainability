import unittest
from mbpp_967_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check("aeiouAEIOU"), 'accepted')

    def test_edge_case1(self):
        self.assertEqual(check("AEIOU"), 'accepted')

    def test_edge_case2(self):
        self.assertEqual(check("aeiou"), 'accepted')

    def test_edge_case3(self):
        self.assertEqual(check("AEIOUaeiou"), 'accepted')

    def test_edge_case4(self):
        self.assertEqual(check("AEIOUAEIOU"), 'accepted')

    def test_edge_case5(self):
        self.assertEqual(check("aeiouaeiou"), 'accepted')

    def test_edge_case6(self):
        self.assertEqual(check("AEIOUAEIOUaeiou"), 'accepted')

    def test_edge_case7(self):
        self.assertEqual(check("AEIOUAEIOUAEIOU"), 'accepted')

    def test_edge_case8(self):
        self.assertEqual(check("aeiouaeiouaeiou"), 'accepted')

    def test_edge_case9(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUaeiou"), 'accepted')

    def test_edge_case10(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUAEIOU"), 'accepted')

    def test_edge_case11(self):
        self.assertEqual(check("aeiouaeiouaeiouaeiou"), 'accepted')

    def test_edge_case12(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUAEIOUaeiou"), 'accepted')

    def test_edge_case13(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUAEIOUAEIOU"), 'accepted')

    def test_edge_case14(self):
        self.assertEqual(check("aeiouaeiouaeiouaeiouaeiou"), 'accepted')

    def test_edge_case15(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUAEIOUAEIOUaeiou"), 'accepted')

    def test_edge_case16(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUAEIOUAEIOUAEIOU"), 'accepted')

    def test_edge_case17(self):
        self.assertEqual(check("aeiouaeiouaeiouaeiouaeiouaeiou"), 'accepted')

    def test_edge_case18(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOU"), 'accepted')

    def test_edge_case19(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOU"), 'accepted')

    def test_edge_case20(self):
        self.assertEqual(check("aeiouaeiouaeiouaeiouaeiouaeiouaeiou"), 'accepted')

    def test_edge_case21(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOU"), 'accepted')

    def test_edge_case22(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOU"), 'accepted')

    def test_edge_case23(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOU"), 'accepted')

    def test_edge_case24(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOU"), 'accepted')

    def test_edge_case25(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOU"), 'accepted')

    def test_edge_case26(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOU"), 'accepted')

    def test_edge_case27(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOU"), 'accepted')

    def test_edge_case28(self):
        self.assertEqual(check("AEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAEIOUAE