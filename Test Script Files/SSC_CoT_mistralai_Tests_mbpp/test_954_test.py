import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(profit_amount(100, 50), 50)
        self.assertEqual(profit_amount(50, 30), 20)
        self.assertEqual(profit_amount(200, 250), -50)

    def test_edge_cases(self):
        self.assertEqual(profit_amount(0, 1), None)
        self.assertEqual(profit_amount(1, 0), None)
        self.assertEqual(profit_amount(1, 1), None)

    def test_boundary_cases(self):
        self.assertEqual(profit_amount(1000000000, 999999999), 1)
        self.assertEqual(profit_amount(999999999, 1000000000), -1)
