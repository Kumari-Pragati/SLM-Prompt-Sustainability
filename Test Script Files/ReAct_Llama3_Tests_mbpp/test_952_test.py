import unittest
from mbpp_952_code import nCr_mod_p

class TestNcrModP(unittest.TestCase):
    def test_nCr_mod_p_typical_case(self):
        self.assertEqual(nCr_mod_p(10, 3, 7), 10)

    def test_nCr_mod_p_edge_case(self):
        self.assertEqual(nCr_mod_p(10, 10, 7), 1)

    def test_nCr_mod_p_edge_case2(self):
        self.assertEqual(nCr_mod_p(10, 0, 7), 1)

    def test_nCr_mod_p_edge_case3(self):
        self.assertEqual(nCr_mod_p(10, 11, 7), 0)

    def test_nCr_mod_p_edge_case4(self):
        self.assertEqual(nCr_mod_p(10, 10, 10), 1)

    def test_nCr_mod_p_edge_case5(self):
        self.assertEqual(nCr_mod_p(10, 10, 11), 1)

    def test_nCr_mod_p_edge_case6(self):
        self.assertEqual(nCr_mod_p(10, 10, 12), 1)

    def test_nCr_mod_p_edge_case7(self):
        self.assertEqual(nCr_mod_p(10, 10, 13), 1)

    def test_nCr_mod_p_edge_case8(self):
        self.assertEqual(nCr_mod_p(10, 10, 14), 1)

    def test_nCr_mod_p_edge_case9(self):
        self.assertEqual(nCr_mod_p(10, 10, 15), 1)

    def test_nCr_mod_p_edge_case10(self):
        self.assertEqual(nCr_mod_p(10, 10, 16), 1)

    def test_nCr_mod_p_edge_case11(self):
        self.assertEqual(nCr_mod_p(10, 10, 17), 1)

    def test_nCr_mod_p_edge_case12(self):
        self.assertEqual(nCr_mod_p(10, 10, 18), 1)

    def test_nCr_mod_p_edge_case13(self):
        self.assertEqual(nCr_mod_p(10, 10, 19), 1)

    def test_nCr_mod_p_edge_case14(self):
        self.assertEqual(nCr_mod_p(10, 10, 20), 1)

    def test_nCr_mod_p_edge_case15(self):
        self.assertEqual(nCr_mod_p(10, 10, 21), 1)

    def test_nCr_mod_p_edge_case16(self):
        self.assertEqual(nCr_mod_p(10, 10, 22), 1)

    def test_nCr_mod_p_edge_case17(self):
        self.assertEqual(nCr_mod_p(10, 10, 23), 1)

    def test_nCr_mod_p_edge_case18(self):
        self.assertEqual(nCr_mod_p(10, 10, 24), 1)

    def test_nCr_mod_p_edge_case19(self):
        self.assertEqual(nCr_mod_p(10, 10, 25), 1)

    def test_nCr_mod_p_edge_case20(self):
        self.assertEqual(nCr_mod_p(10, 10, 26), 1)

    def test_nCr_mod_p_edge_case21(self):
        self.assertEqual(nCr_mod_p(10, 10, 27), 1)

    def test_nCr_mod_p_edge_case22(self):
        self.assertEqual(nCr_mod_p(10, 10, 28), 1)

    def test_nCr_mod_p_edge_case23(self):
        self.assertEqual(nCr_mod_p(10, 10, 29), 1)

    def test_nCr_mod_p_edge_case24(self):
        self.assertEqual(nCr_mod_p(10, 10, 30), 1)

    def test_nCr_mod_p_edge_case25(self):
        self.assertEqual(nCr_mod_p(10, 10, 31), 1)

    def test_nCr_mod_p_edge_case26(self):
        self.assertEqual(nCr_mod_p(10, 10, 32), 1)

    def test_nCr_mod_p_edge_case27(self):
        self.assertEqual(nCr_mod_p(10, 10, 33), 1)

    def test_nCr_mod_p_edge_case28(self):
        self.assertEqual(nCr_mod_p(10, 10, 34), 1)

    def test_nCr_mod_p_edge_case29(self):
        self.assertEqual(nCr_mod_p(10, 10, 35), 1)

    def test_nCr_mod_p_edge_case30(self):
        self.assertEqual(nCr_mod_p(10, 10, 36), 1)

    def test_nCr_mod_p_edge_case31(self):
        self.assertEqual(nCr_mod_p(10, 10, 37), 1)

    def test_nCr_mod_p_edge_case