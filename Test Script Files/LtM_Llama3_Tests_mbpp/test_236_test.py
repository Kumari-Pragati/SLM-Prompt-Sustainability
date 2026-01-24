import unittest
from mbpp_236_code import No_of_Triangle

class TestNo_of_Triangle(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(No_of_Triangle(5, 2), 6)

    def test_edge_case_N_equal_K(self):
        self.assertEqual(No_of_Triangle(2, 2), 1)

    def test_edge_case_N_less_than_K(self):
        self.assertEqual(No_of_Triangle(1, 2), -1)

    def test_edge_case_N_equal_to_2K(self):
        self.assertEqual(No_of_Triangle(4, 2), 2)

    def test_edge_case_N_equal_to_2K_plus_1(self):
        self.assertEqual(No_of_Triangle(5, 2), 3)

    def test_edge_case_N_equal_to_2K_plus_2(self):
        self.assertEqual(No_of_Triangle(6, 2), 4)

    def test_edge_case_N_equal_to_2K_plus_3(self):
        self.assertEqual(No_of_Triangle(7, 2), 5)

    def test_edge_case_N_equal_to_2K_plus_4(self):
        self.assertEqual(No_of_Triangle(8, 2), 6)

    def test_edge_case_N_equal_to_2K_plus_5(self):
        self.assertEqual(No_of_Triangle(9, 2), 7)

    def test_edge_case_N_equal_to_2K_plus_6(self):
        self.assertEqual(No_of_Triangle(10, 2), 8)

    def test_edge_case_N_equal_to_2K_plus_7(self):
        self.assertEqual(No_of_Triangle(11, 2), 9)

    def test_edge_case_N_equal_to_2K_plus_8(self):
        self.assertEqual(No_of_Triangle(12, 2), 10)

    def test_edge_case_N_equal_to_2K_plus_9(self):
        self.assertEqual(No_of_Triangle(13, 2), 11)

    def test_edge_case_N_equal_to_2K_plus_10(self):
        self.assertEqual(No_of_Triangle(14, 2), 12)

    def test_edge_case_N_equal_to_2K_plus_11(self):
        self.assertEqual(No_of_Triangle(15, 2), 13)

    def test_edge_case_N_equal_to_2K_plus_12(self):
        self.assertEqual(No_of_Triangle(16, 2), 14)

    def test_edge_case_N_equal_to_2K_plus_13(self):
        self.assertEqual(No_of_Triangle(17, 2), 15)

    def test_edge_case_N_equal_to_2K_plus_14(self):
        self.assertEqual(No_of_Triangle(18, 2), 16)

    def test_edge_case_N_equal_to_2K_plus_15(self):
        self.assertEqual(No_of_Triangle(19, 2), 17)

    def test_edge_case_N_equal_to_2K_plus_16(self):
        self.assertEqual(No_of_Triangle(20, 2), 18)

    def test_edge_case_N_equal_to_2K_plus_17(self):
        self.assertEqual(No_of_Triangle(21, 2), 19)

    def test_edge_case_N_equal_to_2K_plus_18(self):
        self.assertEqual(No_of_Triangle(22, 2), 20)

    def test_edge_case_N_equal_to_2K_plus_19(self):
        self.assertEqual(No_of_Triangle(23, 2), 21)

    def test_edge_case_N_equal_to_2K_plus_20(self):
        self.assertEqual(No_of_Triangle(24, 2), 22)

    def test_edge_case_N_equal_to_2K_plus_21(self):
        self.assertEqual(No_of_Triangle(25, 2), 23)

    def test_edge_case_N_equal_to_2K_plus_22(self):
        self.assertEqual(No_of_Triangle(26, 2), 24)

    def test_edge_case_N_equal_to_2K_plus_23(self):
        self.assertEqual(No_of_Triangle(27, 2), 25)

    def test_edge_case_N_equal_to_2K_plus_24(self):
        self.assertEqual(No_of_Triangle(28, 2), 26)

    def test_edge_case_N_equal_to_2K_plus_25(self):
        self.assertEqual(No_of_Triangle(29, 2), 27)

    def test_edge_case_N_equal_to_2K_plus_26(self):
        self.assertEqual(No_of_Triangle(30, 2), 28)

    def test_edge_case_N_equal_to_2K_plus_27(self):
        self.assertEqual(No_of_Triangle(31, 2), 29)