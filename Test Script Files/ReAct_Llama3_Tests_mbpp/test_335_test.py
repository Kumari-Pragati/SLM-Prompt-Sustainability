import unittest
from mbpp_335_code import ap_sum

class TestApSum(unittest.TestCase):

    def test_ap_sum_typical(self):
        self.assertEqual(ap_sum(1, 5, 2), 9)

    def test_ap_sum_edge_case(self):
        self.assertEqual(ap_sum(1, 1, 2), 1)

    def test_ap_sum_edge_case2(self):
        self.assertEqual(ap_sum(1, 0, 2), 0)

    def test_ap_sum_edge_case3(self):
        self.assertEqual(ap_sum(1, 10, 2), 55)

    def test_ap_sum_edge_case4(self):
        self.assertEqual(ap_sum(1, -1, 2), 0)

    def test_ap_sum_edge_case5(self):
        self.assertEqual(ap_sum(1, 1, 0), 0)

    def test_ap_sum_edge_case6(self):
        self.assertEqual(ap_sum(1, 1, -2), 0)

    def test_ap_sum_edge_case7(self):
        self.assertEqual(ap_sum(1, 1, 2), 3)

    def test_ap_sum_edge_case8(self):
        self.assertEqual(ap_sum(1, 1, 2), 3)

    def test_ap_sum_edge_case9(self):
        self.assertEqual(ap_sum(1, 1, 2), 3)

    def test_ap_sum_edge_case10(self):
        self.assertEqual(ap_sum(1, 1, 2), 3)
