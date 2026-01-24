import unittest
from mbpp_520_code import get_lcm

class TestGetLcm(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_lcm([2, 3]), 6)

    def test_edge_case(self):
        self.assertEqual(get_lcm([1, 1]), 1)

    def test_edge_case2(self):
        self.assertEqual(get_lcm([10, 15]), 30)

    def test_edge_case3(self):
        self.assertEqual(get_lcm([20, 25]), 100)

    def test_edge_case4(self):
        self.assertEqual(get_lcm([5, 7]), 35)

    def test_edge_case5(self):
        self.assertEqual(get_lcm([3, 4]), 12)

    def test_edge_case6(self):
        self.assertEqual(get_lcm([6, 8]), 24)

    def test_edge_case7(self):
        self.assertEqual(get_lcm([9, 10]), 90)

    def test_edge_case8(self):
        self.assertEqual(get_lcm([11, 12]), 132)

    def test_edge_case9(self):
        self.assertEqual(get_lcm([13, 14]), 182)

    def test_edge_case10(self):
        self.assertEqual(get_lcm([15, 16]), 240)

    def test_edge_case11(self):
        self.assertEqual(get_lcm([17, 18]), 306)

    def test_edge_case12(self):
        self.assertEqual(get_lcm([19, 20]), 380)

    def test_edge_case13(self):
        self.assertEqual(get_lcm([21, 22]), 462)

    def test_edge_case14(self):
        self.assertEqual(get_lcm([23, 24]), 552)

    def test_edge_case15(self):
        self.assertEqual(get_lcm([25, 26]), 650)

    def test_edge_case16(self):
        self.assertEqual(get_lcm([27, 28]), 756)

    def test_edge_case17(self):
        self.assertEqual(get_lcm([29, 30]), 870)

    def test_edge_case18(self):
        self.assertEqual(get_lcm([31, 32]), 992)

    def test_edge_case19(self):
        self.assertEqual(get_lcm([33, 34]), 1122)

    def test_edge_case20(self):
        self.assertEqual(get_lcm([35, 36]), 1260)
