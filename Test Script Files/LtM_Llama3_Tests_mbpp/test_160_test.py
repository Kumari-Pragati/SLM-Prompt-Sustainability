import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(solution(2, 3, 6), ("x = ", 1, ", y = ", 2))
    def test_edge(self):
        self.assertEqual(solution(2, 3, 5), ("x = ", 2, ", y = ", 1))
    def test_edge2(self):
        self.assertEqual(solution(2, 3, 4), ("No solution"))
    def test_edge3(self):
        self.assertEqual(solution(2, 3, 3), ("x = ", 1, ", y = ", 1))
    def test_edge4(self):
        self.assertEqual(solution(2, 3, 2), ("No solution"))
    def test_edge5(self):
        self.assertEqual(solution(2, 3, 1), ("No solution"))
    def test_edge6(self):
        self.assertEqual(solution(2, 3, 0), ("No solution"))
    def test_edge7(self):
        self.assertEqual(solution(2, 3, -1), ("No solution"))
    def test_edge8(self):
        self.assertEqual(solution(2, 3, -2), ("No solution"))
    def test_edge9(self):
        self.assertEqual(solution(2, 3, -3), ("No solution"))
    def test_edge10(self):
        self.assertEqual(solution(2, 3, -4), ("No solution"))
    def test_edge11(self):
        self.assertEqual(solution(2, 3, -5), ("No solution"))
    def test_edge12(self):
        self.assertEqual(solution(2, 3, -6), ("No solution"))
    def test_edge13(self):
        self.assertEqual(solution(2, 3, -7), ("No solution"))
    def test_edge14(self):
        self.assertEqual(solution(2, 3, -8), ("No solution"))
    def test_edge15(self):
        self.assertEqual(solution(2, 3, -9), ("No solution"))
    def test_edge16(self):
        self.assertEqual(solution(2, 3, -10), ("No solution"))
    def test_edge17(self):
        self.assertEqual(solution(2, 3, -11), ("No solution"))
    def test_edge18(self):
        self.assertEqual(solution(2, 3, -12), ("No solution"))
    def test_edge19(self):
        self.assertEqual(solution(2, 3, -13), ("No solution"))
    def test_edge20(self):
        self.assertEqual(solution(2, 3, -14), ("No solution"))
    def test_edge21(self):
        self.assertEqual(solution(2, 3, -15), ("No solution"))
    def test_edge22(self):
        self.assertEqual(solution(2, 3, -16), ("No solution"))
    def test_edge23(self):
        self.assertEqual(solution(2, 3, -17), ("No solution"))
    def test_edge24(self):
        self.assertEqual(solution(2, 3, -18), ("No solution"))
    def test_edge25(self):
        self.assertEqual(solution(2, 3, -19), ("No solution"))
    def test_edge26(self):
        self.assertEqual(solution(2, 3, -20), ("No solution"))
    def test_edge27(self):
        self.assertEqual(solution(2, 3, -21), ("No solution"))
    def test_edge28(self):
        self.assertEqual(solution(2, 3, -22), ("No solution"))
    def test_edge29(self):
        self.assertEqual(solution(2, 3, -23), ("No solution"))
    def test_edge30(self):
        self.assertEqual(solution(2, 3, -24), ("No solution"))
    def test_edge31(self):
        self.assertEqual(solution(2, 3, -25), ("No solution"))
    def test_edge32(self):
        self.assertEqual(solution(2, 3, -26), ("No solution"))
    def test_edge33(self):
        self.assertEqual(solution(2, 3, -27), ("No solution"))
    def test_edge34(self):
        self.assertEqual(solution(2, 3, -28), ("No solution"))
    def test_edge35(self):
        self.assertEqual(solution(2, 3, -29), ("No solution"))
    def test_edge36(self):
        self.assertEqual(solution(2, 3, -30), ("No solution"))
    def test_edge37(self):
        self.assertEqual(solution(2, 3, -31), ("No solution"))
    def test_edge38(self):
        self.assertEqual(solution(2, 3, -32), ("No solution"))
    def test_edge39(self):
        self.assertEqual(solution(2, 3, -33), ("No solution"))
    def test_edge40(self):
        self.assertEqual(solution(2, 3, -34),