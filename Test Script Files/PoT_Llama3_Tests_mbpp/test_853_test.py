import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_of_odd_Factors(12), 2)

    def test_edge_case(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)

    def test_edge_case2(self):
        self.assertEqual(sum_of_odd_Factors(2), 3)

    def test_edge_case3(self):
        self.assertEqual(sum_of_odd_Factors(3), 4)

    def test_edge_case4(self):
        self.assertEqual(sum_of_odd_Factors(4), 3)

    def test_edge_case5(self):
        self.assertEqual(sum_of_odd_Factors(5), 4)

    def test_edge_case6(self):
        self.assertEqual(sum_of_odd_Factors(6), 3)

    def test_edge_case7(self):
        self.assertEqual(sum_of_odd_Factors(7), 4)

    def test_edge_case8(self):
        self.assertEqual(sum_of_odd_Factors(8), 3)

    def test_edge_case9(self):
        self.assertEqual(sum_of_odd_Factors(9), 4)

    def test_edge_case10(self):
        self.assertEqual(sum_of_odd_Factors(10), 3)

    def test_edge_case11(self):
        self.assertEqual(sum_of_odd_Factors(11), 4)

    def test_edge_case12(self):
        self.assertEqual(sum_of_odd_Factors(12), 2)

    def test_edge_case13(self):
        self.assertEqual(sum_of_odd_Factors(13), 4)

    def test_edge_case14(self):
        self.assertEqual(sum_of_odd_Factors(14), 3)

    def test_edge_case15(self):
        self.assertEqual(sum_of_odd_Factors(15), 4)

    def test_edge_case16(self):
        self.assertEqual(sum_of_odd_Factors(16), 3)

    def test_edge_case17(self):
        self.assertEqual(sum_of_odd_Factors(17), 4)

    def test_edge_case18(self):
        self.assertEqual(sum_of_odd_Factors(18), 3)

    def test_edge_case19(self):
        self.assertEqual(sum_of_odd_Factors(19), 4)

    def test_edge_case20(self):
        self.assertEqual(sum_of_odd_Factors(20), 3)
