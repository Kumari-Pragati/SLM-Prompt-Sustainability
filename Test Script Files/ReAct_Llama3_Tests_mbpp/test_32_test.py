import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_Prime_Factors(100), 5)

    def test_edge_case_1(self):
        self.assertEqual(max_Prime_Factors(2), 2)

    def test_edge_case_2(self):
        self.assertEqual(max_Prime_Factors(3), 3)

    def test_edge_case_3(self):
        self.assertEqual(max_Prime_Factors(4), 2)

    def test_edge_case_4(self):
        self.assertEqual(max_Prime_Factors(9), 3)

    def test_edge_case_5(self):
        self.assertEqual(max_Prime_Factors(25), 5)

    def test_edge_case_6(self):
        self.assertEqual(max_Prime_Factors(36), 3)

    def test_edge_case_7(self):
        self.assertEqual(max_Prime_Factors(48), 2)

    def test_edge_case_8(self):
        self.assertEqual(max_Prime_Factors(49), 7)

    def test_edge_case_9(self):
        self.assertEqual(max_Prime_Factors(50), 5)

    def test_edge_case_10(self):
        self.assertEqual(max_Prime_Factors(51), 3)

    def test_edge_case_11(self):
        self.assertEqual(max_Prime_Factors(52), 2)

    def test_edge_case_12(self):
        self.assertEqual(max_Prime_Factors(53), 53)

    def test_edge_case_13(self):
        self.assertEqual(max_Prime_Factors(54), 3)

    def test_edge_case_14(self):
        self.assertEqual(max_Prime_Factors(55), 5)

    def test_edge_case_15(self):
        self.assertEqual(max_Prime_Factors(56), 2)

    def test_edge_case_16(self):
        self.assertEqual(max_Prime_Factors(57), 3)

    def test_edge_case_17(self):
        self.assertEqual(max_Prime_Factors(58), 2)

    def test_edge_case_18(self):
        self.assertEqual(max_Prime_Factors(59), 59)

    def test_edge_case_19(self):
        self.assertEqual(max_Prime_Factors(60), 3)

    def test_edge_case_20(self):
        self.assertEqual(max_Prime_Factors(61), 61)

    def test_edge_case_21(self):
        self.assertEqual(max_Prime_Factors(62), 2)

    def test_edge_case_22(self):
        self.assertEqual(max_Prime_Factors(63), 3)

    def test_edge_case_23(self):
        self.assertEqual(max_Prime_Factors(64), 2)

    def test_edge_case_24(self):
        self.assertEqual(max_Prime_Factors(65), 5)

    def test_edge_case_25(self):
        self.assertEqual(max_Prime_Factors(66), 2)

    def test_edge_case_26(self):
        self.assertEqual(max_Prime_Factors(67), 67)

    def test_edge_case_27(self):
        self.assertEqual(max_Prime_Factors(68), 2)

    def test_edge_case_28(self):
        self.assertEqual(max_Prime_Factors(69), 3)

    def test_edge_case_29(self):
        self.assertEqual(max_Prime_Factors(70), 2)

    def test_edge_case_30(self):
        self.assertEqual(max_Prime_Factors(71), 71)

    def test_edge_case_31(self):
        self.assertEqual(max_Prime_Factors(72), 2)

    def test_edge_case_32(self):
        self.assertEqual(max_Prime_Factors(73), 73)

    def test_edge_case_33(self):
        self.assertEqual(max_Prime_Factors(74), 2)

    def test_edge_case_34(self):
        self.assertEqual(max_Prime_Factors(75), 3)

    def test_edge_case_35(self):
        self.assertEqual(max_Prime_Factors(76), 2)

    def test_edge_case_36(self):
        self.assertEqual(max_Prime_Factors(77), 7)

    def test_edge_case_37(self):
        self.assertEqual(max_Prime_Factors(78), 2)

    def test_edge_case_38(self):
        self.assertEqual(max_Prime_Factors(79), 79)

    def test_edge_case_39(self):
        self.assertEqual(max_Prime_Factors(80), 2)

    def test_edge_case_40(self):
        self.assertEqual(max_Prime_Factors(81), 3)

    def test_edge_case_41(self):
        self.assertEqual(max_Prime_Factors(82), 2)

    def test_edge_case_42(self):
        self.assertEqual(max_Prime_Factors(83), 83)

    def test_edge_case_43(self):
        self.assertEqual