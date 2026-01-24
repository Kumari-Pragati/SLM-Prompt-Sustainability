import unittest
from mbpp_236_code import No_of_Triangle

class TestNo_of_Triangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(No_of_Triangle(10, 3), 6)

    def test_edge_case_N_eq_K(self):
        self.assertEqual(No_of_Triangle(3, 3), 0)

    def test_edge_case_N_eq_2K(self):
        self.assertEqual(No_of_Triangle(6, 3), 3)

    def test_edge_case_N_eq_2K_plus_1(self):
        self.assertEqual(No_of_Triangle(7, 3), 6)

    def test_edge_case_N_eq_2K_plus_2(self):
        self.assertEqual(No_of_Triangle(8, 3), 6)

    def test_edge_case_N_eq_2K_plus_3(self):
        self.assertEqual(No_of_Triangle(9, 3), 6)

    def test_edge_case_N_eq_2K_plus_4(self):
        self.assertEqual(No_of_Triangle(10, 3), 6)

    def test_edge_case_N_eq_2K_plus_5(self):
        self.assertEqual(No_of_Triangle(11, 3), 6)

    def test_edge_case_N_eq_2K_plus_6(self):
        self.assertEqual(No_of_Triangle(12, 3), 6)

    def test_edge_case_N_eq_2K_plus_7(self):
        self.assertEqual(No_of_Triangle(13, 3), 6)

    def test_edge_case_N_eq_2K_plus_8(self):
        self.assertEqual(No_of_Triangle(14, 3), 6)

    def test_edge_case_N_eq_2K_plus_9(self):
        self.assertEqual(No_of_Triangle(15, 3), 6)

    def test_edge_case_N_eq_2K_plus_10(self):
        self.assertEqual(No_of_Triangle(16, 3), 6)

    def test_edge_case_N_eq_2K_plus_11(self):
        self.assertEqual(No_of_Triangle(17, 3), 6)

    def test_edge_case_N_eq_2K_plus_12(self):
        self.assertEqual(No_of_Triangle(18, 3), 6)

    def test_edge_case_N_eq_2K_plus_13(self):
        self.assertEqual(No_of_Triangle(19, 3), 6)

    def test_edge_case_N_eq_2K_plus_14(self):
        self.assertEqual(No_of_Triangle(20, 3), 6)

    def test_edge_case_N_eq_2K_plus_15(self):
        self.assertEqual(No_of_Triangle(21, 3), 6)

    def test_edge_case_N_eq_2K_plus_16(self):
        self.assertEqual(No_of_Triangle(22, 3), 6)

    def test_edge_case_N_eq_2K_plus_17(self):
        self.assertEqual(No_of_Triangle(23, 3), 6)

    def test_edge_case_N_eq_2K_plus_18(self):
        self.assertEqual(No_of_Triangle(24, 3), 6)

    def test_edge_case_N_eq_2K_plus_19(self):
        self.assertEqual(No_of_Triangle(25, 3), 6)

    def test_edge_case_N_eq_2K_plus_20(self):
        self.assertEqual(No_of_Triangle(26, 3), 6)

    def test_edge_case_N_eq_2K_plus_21(self):
        self.assertEqual(No_of_Triangle(27, 3), 6)

    def test_edge_case_N_eq_2K_plus_22(self):
        self.assertEqual(No_of_Triangle(28, 3), 6)

    def test_edge_case_N_eq_2K_plus_23(self):
        self.assertEqual(No_of_Triangle(29, 3), 6)

    def test_edge_case_N_eq_2K_plus_24(self):
        self.assertEqual(No_of_Triangle(30, 3), 6)

    def test_edge_case_N_eq_2K_plus_25(self):
        self.assertEqual(No_of_Triangle(31, 3), 6)

    def test_edge_case_N_eq_2K_plus_26(self):
        self.assertEqual(No_of_Triangle(32, 3), 6)

    def test_edge_case_N_eq_2K_plus_27(self):
        self.assertEqual(No_of_Triangle(33, 3), 6)

    def test_edge_case_N_eq_2K_plus_28(self):
        self.assertEqual(No_of_Triangle(34, 3), 6)

    def test_edge_case_N_eq_2K_plus_29(self):
        self.assertEqual(No_of_Triangle