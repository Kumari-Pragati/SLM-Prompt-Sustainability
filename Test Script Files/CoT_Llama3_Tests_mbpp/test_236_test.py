import unittest
from mbpp_236_code import No_of_Triangle

class TestNo_of_Triangle(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(No_of_Triangle(5, 2), 6)

    def test_edge_case_N_eq_K(self):
        self.assertEqual(No_of_Triangle(2, 2), 1)

    def test_edge_case_N_eq_2K(self):
        self.assertEqual(No_of_Triangle(4, 2), 2)

    def test_edge_case_N_eq_3K(self):
        self.assertEqual(No_of_Triangle(6, 2), 3)

    def test_edge_case_N_eq_4K(self):
        self.assertEqual(No_of_Triangle(8, 2), 4)

    def test_edge_case_N_eq_5K(self):
        self.assertEqual(No_of_Triangle(10, 2), 5)

    def test_edge_case_N_eq_6K(self):
        self.assertEqual(No_of_Triangle(12, 2), 6)

    def test_edge_case_N_eq_7K(self):
        self.assertEqual(No_of_Triangle(14, 2), 7)

    def test_edge_case_N_eq_8K(self):
        self.assertEqual(No_of_Triangle(16, 2), 8)

    def test_edge_case_N_eq_9K(self):
        self.assertEqual(No_of_Triangle(18, 2), 9)

    def test_edge_case_N_eq_10K(self):
        self.assertEqual(No_of_Triangle(20, 2), 10)

    def test_invalid_input_N_eq_0(self):
        self.assertEqual(No_of_Triangle(0, 2), -1)

    def test_invalid_input_N_eq_1(self):
        self.assertEqual(No_of_Triangle(1, 2), -1)

    def test_invalid_input_N_eq_2(self):
        self.assertEqual(No_of_Triangle(2, 2), 1)

    def test_invalid_input_N_eq_3(self):
        self.assertEqual(No_of_Triangle(3, 2), 2)

    def test_invalid_input_N_eq_4(self):
        self.assertEqual(No_of_Triangle(4, 2), 2)

    def test_invalid_input_N_eq_5(self):
        self.assertEqual(No_of_Triangle(5, 2), 6)

    def test_invalid_input_N_eq_6(self):
        self.assertEqual(No_of_Triangle(6, 2), 6)

    def test_invalid_input_N_eq_7(self):
        self.assertEqual(No_of_Triangle(7, 2), 7)

    def test_invalid_input_N_eq_8(self):
        self.assertEqual(No_of_Triangle(8, 2), 8)

    def test_invalid_input_N_eq_9(self):
        self.assertEqual(No_of_Triangle(9, 2), 9)

    def test_invalid_input_N_eq_10(self):
        self.assertEqual(No_of_Triangle(10, 2), 10)

    def test_invalid_input_N_eq_11(self):
        self.assertEqual(No_of_Triangle(11, 2), 11)

    def test_invalid_input_N_eq_12(self):
        self.assertEqual(No_of_Triangle(12, 2), 12)

    def test_invalid_input_N_eq_13(self):
        self.assertEqual(No_of_Triangle(13, 2), 13)

    def test_invalid_input_N_eq_14(self):
        self.assertEqual(No_of_Triangle(14, 2), 14)

    def test_invalid_input_N_eq_15(self):
        self.assertEqual(No_of_Triangle(15, 2), 15)

    def test_invalid_input_N_eq_16(self):
        self.assertEqual(No_of_Triangle(16, 2), 16)

    def test_invalid_input_N_eq_17(self):
        self.assertEqual(No_of_Triangle(17, 2), 17)

    def test_invalid_input_N_eq_18(self):
        self.assertEqual(No_of_Triangle(18, 2), 18)

    def test_invalid_input_N_eq_19(self):
        self.assertEqual(No_of_Triangle(19, 2), 19)

    def test_invalid_input_N_eq_20(self):
        self.assertEqual(No_of_Triangle(20, 2), 20)
