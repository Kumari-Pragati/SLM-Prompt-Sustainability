import unittest
from mbpp_967_code import check

class TestCheckFunction(unittest.TestCase):
    def test_accepted(self):
        self.assertEqual(check("aeiouAEIOU"), 'accepted')

    def test_not_accepted(self):
        self.assertEqual(check("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"), 'not accepted')

    def test_edge_case(self):
        self.assertEqual(check("aeiouAEIOUa"), 'accepted')

    def test_edge_case2(self):
        self.assertEqual(check("AEIOUaeiou"), 'accepted')

    def test_edge_case3(self):
        self.assertEqual(check("AEIOUaeioua"), 'accepted')

    def test_edge_case4(self):
        self.assertEqual(check("AEIOUaeiouAEIOU"), 'accepted')

    def test_edge_case5(self):
        self.assertEqual(check("AEIOUaeiouAEIOUa"), 'accepted')

    def test_edge_case6(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOU"), 'accepted')

    def test_edge_case7(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUa"), 'accepted')

    def test_edge_case8(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOU"), 'accepted')

    def test_edge_case9(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUA"), 'accepted')

    def test_edge_case10(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAa"), 'accepted')

    def test_edge_case11(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOU"), 'accepted')

    def test_edge_case12(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOUA"), 'accepted')

    def test_edge_case13(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOUAa"), 'accepted')

    def test_edge_case14(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOUAaAEIOU"), 'accepted')

    def test_edge_case15(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOUAaAEIOUA"), 'accepted')

    def test_edge_case16(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOUAaAEIOUAa"), 'accepted')

    def test_edge_case17(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOUAaAEIOUAaAEIOU"), 'accepted')

    def test_edge_case18(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOUAaAEIOUAaAEIOUA"), 'accepted')

    def test_edge_case19(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOUAaAEIOUAaAEIOUAa"), 'accepted')

    def test_edge_case20(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOUAaAEIOUAaAEIOUAaAEIOU"), 'accepted')

    def test_edge_case21(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOUAaAEIOUAaAEIOUAaAEIOUA"), 'accepted')

    def test_edge_case22(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOUAaAEIOUAaAEIOUAaAEIOUAa"), 'accepted')

    def test_edge_case23(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOUAaAEIOUAaAEIOUAaAEIOUAaAEIOU"), 'accepted')

    def test_edge_case24(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOUAaAEIOUAaAEIOUAaAEIOUAaAEIOUA"), 'accepted')

    def test_edge_case25(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOUAaAEIOUAaAEIOUAaAEIOUAaAEIOUAa"), 'accepted')

    def test_edge_case26(self):
        self.assertEqual(check("AEIOUaeiouAEIOUAEIOUAEIOUAaAEIOUAaAE