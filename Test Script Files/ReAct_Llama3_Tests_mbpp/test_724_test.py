import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):

    def test_power_base_sum_typical(self):
        self.assertEqual(power_base_sum(2, 3), 8)

    def test_power_base_sum_edge_case(self):
        self.assertEqual(power_base_sum(1, 1), 1)

    def test_power_base_sum_edge_case2(self):
        self.assertEqual(power_base_sum(0, 1), 0)

    def test_power_base_sum_edge_case3(self):
        self.assertEqual(power_base_sum(-1, 1), -1)

    def test_power_base_sum_edge_case4(self):
        self.assertEqual(power_base_sum(1, 0), 1)

    def test_power_base_sum_edge_case5(self):
        self.assertEqual(power_base_sum(0, 0), 0)

    def test_power_base_sum_edge_case6(self):
        self.assertEqual(power_base_sum(-1, 0), 0)

    def test_power_base_sum_edge_case7(self):
        self.assertEqual(power_base_sum(1, -1), 1)

    def test_power_base_sum_edge_case8(self):
        self.assertEqual(power_base_sum(-1, -1), -1)

    def test_power_base_sum_edge_case9(self):
        self.assertEqual(power_base_sum(0, -1), 0)

    def test_power_base_sum_edge_case10(self):
        self.assertEqual(power_base_sum(-1, -1), -1)

    def test_power_base_sum_edge_case11(self):
        self.assertEqual(power_base_sum(1, 1), 1)

    def test_power_base_sum_edge_case12(self):
        self.assertEqual(power_base_sum(-1, 1), -1)

    def test_power_base_sum_edge_case13(self):
        self.assertEqual(power_base_sum(1, -1), 1)

    def test_power_base_sum_edge_case14(self):
        self.assertEqual(power_base_sum(-1, -1), -1)

    def test_power_base_sum_edge_case15(self):
        self.assertEqual(power_base_sum(0, 1), 0)

    def test_power_base_sum_edge_case16(self):
        self.assertEqual(power_base_sum(-1, 1), -1)

    def test_power_base_sum_edge_case17(self):
        self.assertEqual(power_base_sum(1, 1), 1)

    def test_power_base_sum_edge_case18(self):
        self.assertEqual(power_base_sum(-1, -1), -1)

    def test_power_base_sum_edge_case19(self):
        self.assertEqual(power_base_sum(1, 1), 1)

    def test_power_base_sum_edge_case20(self):
        self.assertEqual(power_base_sum(-1, 1), -1)
