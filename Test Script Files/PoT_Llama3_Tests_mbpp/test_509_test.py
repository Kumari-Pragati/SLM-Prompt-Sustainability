import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(average_Odd(10), 5)

    def test_edge_case(self):
        self.assertEqual(average_Odd(2), -1)

    def test_edge_case2(self):
        self.assertEqual(average_Odd(4), -1)

    def test_edge_case3(self):
        self.assertEqual(average_Odd(6), -1)

    def test_edge_case4(self):
        self.assertEqual(average_Odd(8), -1)

    def test_edge_case5(self):
        self.assertEqual(average_Odd(10), -1)

    def test_edge_case6(self):
        self.assertEqual(average_Odd(12), -1)

    def test_edge_case7(self):
        self.assertEqual(average_Odd(14), -1)

    def test_edge_case8(self):
        self.assertEqual(average_Odd(16), -1)

    def test_edge_case9(self):
        self.assertEqual(average_Odd(18), -1)

    def test_edge_case10(self):
        self.assertEqual(average_Odd(20), -1)

    def test_typical_case2(self):
        self.assertEqual(average_Odd(12), 6)

    def test_typical_case3(self):
        self.assertEqual(average_Odd(14), 7)

    def test_typical_case4(self):
        self.assertEqual(average_Odd(16), 8)

    def test_typical_case5(self):
        self.assertEqual(average_Odd(18), 9)

    def test_typical_case6(self):
        self.assertEqual(average_Odd(20), 10)

    def test_edge_case11(self):
        self.assertEqual(average_Odd(0), -1)

    def test_edge_case12(self):
        self.assertEqual(average_Odd(-1), -1)

    def test_edge_case13(self):
        self.assertEqual(average_Odd(-2), -1)

    def test_edge_case14(self):
        self.assertEqual(average_Odd(-4), -1)

    def test_edge_case15(self):
        self.assertEqual(average_Odd(-6), -1)

    def test_edge_case16(self):
        self.assertEqual(average_Odd(-8), -1)

    def test_edge_case17(self):
        self.assertEqual(average_Odd(-10), -1)

    def test_edge_case18(self):
        self.assertEqual(average_Odd(-12), -1)

    def test_edge_case19(self):
        self.assertEqual(average_Odd(-14), -1)

    def test_edge_case20(self):
        self.assertEqual(average_Odd(-16), -1)

    def test_edge_case21(self):
        self.assertEqual(average_Odd(-18), -1)

    def test_edge_case22(self):
        self.assertEqual(average_Odd(-20), -1)
