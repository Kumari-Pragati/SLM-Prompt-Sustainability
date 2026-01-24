import unittest
from mbpp_172_code import count_occurance

class TestCountOccurance(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_occurance("std"), 1)

    def test_edge_case1(self):
        self.assertEqual(count_occurance("stds"), 2)

    def test_edge_case2(self):
        self.assertEqual(count_occurance("stdstd"), 2)

    def test_edge_case3(self):
        self.assertEqual(count_occurance("stdstds"), 3)

    def test_edge_case4(self):
        self.assertEqual(count_occurance("stdstdstd"), 3)

    def test_edge_case5(self):
        self.assertEqual(count_occurance("stdstdstds"), 3)

    def test_edge_case6(self):
        self.assertEqual(count_occurance("stdstdstdstd"), 3)

    def test_edge_case7(self):
        self.assertEqual(count_occurance("stdstdstdstds"), 3)

    def test_edge_case8(self):
        self.assertEqual(count_occurance("stdstdstdstdstd"), 3)

    def test_edge_case9(self):
        self.assertEqual(count_occurance("stdstdstdstdstds"), 3)

    def test_edge_case10(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstd"), 3)

    def test_edge_case11(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstds"), 3)

    def test_edge_case12(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstd"), 3)

    def test_edge_case13(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstds"), 3)

    def test_edge_case14(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstd"), 3)

    def test_edge_case15(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstds"), 3)

    def test_edge_case16(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstd"), 3)

    def test_edge_case17(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstds"), 3)

    def test_edge_case18(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstd"), 3)

    def test_edge_case19(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstds"), 3)

    def test_edge_case20(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstdstd"), 3)

    def test_edge_case21(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstdstds"), 3)

    def test_edge_case22(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstd"), 3)

    def test_edge_case23(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstds"), 3)

    def test_edge_case24(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstd"), 3)

    def test_edge_case25(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstds"), 3)

    def test_edge_case26(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstd"), 3)

    def test_edge_case27(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstds"), 3)

    def test_edge_case28(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstd"), 3)

    def test_edge_case29(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstds"), 3)

    def test_edge_case30(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstd"), 3)

    def test_edge_case31(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstds"), 3)

    def test_edge_case32(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstd"), 3)

    def test_edge_case33(self):
        self.assertEqual(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstds