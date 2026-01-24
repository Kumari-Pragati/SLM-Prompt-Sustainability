import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(solution(2, 3, 10), ("x = ", 2, ", y = ", 1))

    def test_edge_case(self):
        self.assertEqual(solution(2, 3, 5), ("x = ", 1, ", y = ", 1))

    def test_edge_case2(self):
        self.assertEqual(solution(2, 3, 6), ("x = ", 2, ", y = ", 1))

    def test_edge_case3(self):
        self.assertEqual(solution(2, 3, 7), ("No solution"))

    def test_edge_case4(self):
        self.assertEqual(solution(2, 3, 8), ("x = ", 2, ", y = ", 1))

    def test_edge_case5(self):
        self.assertEqual(solution(2, 3, 9), ("x = ", 2, ", y = ", 1))

    def test_edge_case6(self):
        self.assertEqual(solution(2, 3, 11), ("No solution"))

    def test_edge_case7(self):
        self.assertEqual(solution(2, 3, 12), ("No solution"))

    def test_edge_case8(self):
        self.assertEqual(solution(2, 3, 13), ("No solution"))

    def test_edge_case9(self):
        self.assertEqual(solution(2, 3, 14), ("No solution"))

    def test_edge_case10(self):
        self.assertEqual(solution(2, 3, 15), ("No solution"))

    def test_edge_case11(self):
        self.assertEqual(solution(2, 3, 16), ("No solution"))

    def test_edge_case12(self):
        self.assertEqual(solution(2, 3, 17), ("No solution"))

    def test_edge_case13(self):
        self.assertEqual(solution(2, 3, 18), ("No solution"))

    def test_edge_case14(self):
        self.assertEqual(solution(2, 3, 19), ("No solution"))

    def test_edge_case15(self):
        self.assertEqual(solution(2, 3, 20), ("No solution"))

    def test_edge_case16(self):
        self.assertEqual(solution(2, 3, 21), ("No solution"))

    def test_edge_case17(self):
        self.assertEqual(solution(2, 3, 22), ("No solution"))

    def test_edge_case18(self):
        self.assertEqual(solution(2, 3, 23), ("No solution"))

    def test_edge_case19(self):
        self.assertEqual(solution(2, 3, 24), ("No solution"))

    def test_edge_case20(self):
        self.assertEqual(solution(2, 3, 25), ("No solution"))

    def test_edge_case21(self):
        self.assertEqual(solution(2, 3, 26), ("No solution"))

    def test_edge_case22(self):
        self.assertEqual(solution(2, 3, 27), ("No solution"))

    def test_edge_case23(self):
        self.assertEqual(solution(2, 3, 28), ("No solution"))

    def test_edge_case24(self):
        self.assertEqual(solution(2, 3, 29), ("No solution"))

    def test_edge_case25(self):
        self.assertEqual(solution(2, 3, 30), ("No solution"))

    def test_edge_case26(self):
        self.assertEqual(solution(2, 3, 31), ("No solution"))

    def test_edge_case27(self):
        self.assertEqual(solution(2, 3, 32), ("No solution"))

    def test_edge_case28(self):
        self.assertEqual(solution(2, 3, 33), ("No solution"))

    def test_edge_case29(self):
        self.assertEqual(solution(2, 3, 34), ("No solution"))

    def test_edge_case30(self):
        self.assertEqual(solution(2, 3, 35), ("No solution"))

    def test_edge_case31(self):
        self.assertEqual(solution(2, 3, 36), ("No solution"))

    def test_edge_case32(self):
        self.assertEqual(solution(2, 3, 37), ("No solution"))

    def test_edge_case33(self):
        self.assertEqual(solution(2, 3, 38), ("No solution"))

    def test_edge_case34(self):
        self.assertEqual(solution(2, 3, 39), ("No solution"))

    def test_edge_case35(self):
        self.assertEqual(solution(2, 3, 40), ("No solution"))

    def test_edge_case36(self):
        self.assertEqual(solution(2, 3, 41), ("No solution"))

    def test_edge_case37(self):
        self.assertEqual(solution(2, 3, 42), ("No solution"))

    def test_edge_case38(self):