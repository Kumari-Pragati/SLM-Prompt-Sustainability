import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(max_Prime_Factors(100), 5)

    def test_edge_case(self):
        self.assertEqual(max_Prime_Factors(2), 2)
        self.assertEqual(max_Prime_Factors(3), 3)

    def test_edge_case2(self):
        self.assertEqual(max_Prime_Factors(4), 2)
        self.assertEqual(max_Prime_Factors(6), 2)

    def test_edge_case3(self):
        self.assertEqual(max_Prime_Factors(8), 2)
        self.assertEqual(max_Prime_Factors(9), 3)

    def test_edge_case4(self):
        self.assertEqual(max_Prime_Factors(10), 2)
        self.assertEqual(max_Prime_Factors(12), 2)

    def test_edge_case5(self):
        self.assertEqual(max_Prime_Factors(15), 3)
        self.assertEqual(max_Prime_Factors(16), 2)

    def test_edge_case6(self):
        self.assertEqual(max_Prime_Factors(20), 2)
        self.assertEqual(max_Prime_Factors(21), 3)

    def test_edge_case7(self):
        self.assertEqual(max_Prime_Factors(24), 2)
        self.assertEqual(max_Prime_Factors(25), 5)

    def test_edge_case8(self):
        self.assertEqual(max_Prime_Factors(27), 3)
        self.assertEqual(max_Prime_Factors(28), 2)

    def test_edge_case9(self):
        self.assertEqual(max_Prime_Factors(30), 2)
        self.assertEqual(max_Prime_Factors(31), 31)

    def test_edge_case10(self):
        self.assertEqual(max_Prime_Factors(32), 2)
        self.assertEqual(max_Prime_Factors(33), 3)

    def test_edge_case11(self):
        self.assertEqual(max_Prime_Factors(34), 2)
        self.assertEqual(max_Prime_Factors(35), 5)

    def test_edge_case12(self):
        self.assertEqual(max_Prime_Factors(36), 2)
        self.assertEqual(max_Prime_Factors(37), 37)

    def test_edge_case13(self):
        self.assertEqual(max_Prime_Factors(40), 2)
        self.assertEqual(max_Prime_Factors(41), 41)

    def test_edge_case14(self):
        self.assertEqual(max_Prime_Factors(42), 2)
        self.assertEqual(max_Prime_Factors(43), 43)

    def test_edge_case15(self):
        self.assertEqual(max_Prime_Factors(44), 2)
        self.assertEqual(max_Prime_Factors(45), 3)

    def test_edge_case16(self):
        self.assertEqual(max_Prime_Factors(48), 2)
        self.assertEqual(max_Prime_Factors(49), 7)

    def test_edge_case17(self):
        self.assertEqual(max_Prime_Factors(50), 2)
        self.assertEqual(max_Prime_Factors(51), 3)

    def test_edge_case18(self):
        self.assertEqual(max_Prime_Factors(52), 2)
        self.assertEqual(max_Prime_Factors(53), 53)

    def test_edge_case19(self):
        self.assertEqual(max_Prime_Factors(54), 2)
        self.assertEqual(max_Prime_Factors(55), 5)

    def test_edge_case20(self):
        self.assertEqual(max_Prime_Factors(56), 2)
        self.assertEqual(max_Prime_Factors(57), 3)

    def test_edge_case21(self):
        self.assertEqual(max_Prime_Factors(60), 2)
        self.assertEqual(max_Prime_Factors(61), 61)

    def test_edge_case22(self):
        self.assertEqual(max_Prime_Factors(62), 2)
        self.assertEqual(max_Prime_Factors(63), 3)

    def test_edge_case23(self):
        self.assertEqual(max_Prime_Factors(64), 2)
        self.assertEqual(max_Prime_Factors(65), 5)

    def test_edge_case24(self):
        self.assertEqual(max_Prime_Factors(66), 2)
        self.assertEqual(max_Prime_Factors(67), 67)

    def test_edge_case25(self):
        self.assertEqual(max_Prime_Factors(68), 2)
        self.assertEqual(max_Prime_Factors(69), 3)

    def test_edge_case26(self):
        self.assertEqual(max_Prime_Factors(70), 2)
        self.assertEqual(max_Prime_Factors(71), 71)

    def test_edge_case27(self):
        self.assertEqual(max_Prime_Factors(72), 2)
        self.assertEqual(max_Prime_Factors(73), 73)

    def test_edge_case28(self):