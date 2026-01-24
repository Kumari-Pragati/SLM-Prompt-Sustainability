import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):

    def test_positive_typical(self):
        self.assertEqual(profit_amount(10, 5), 5)
        self.assertEqual(profit_amount(20, 15), 5)
        self.assertEqual(profit_amount(30, 25), 5)

    def test_positive_edge(self):
        self.assertEqual(profit_amount(1, 0), 1)
        self.assertEqual(profit_amount(100, 99), 1)

    def test_positive_boundary(self):
        self.assertEqual(profit_amount(0, 0), None)
        self.assertEqual(profit_amount(0, 1), None)
        self.assertEqual(profit_amount(1, 0), 1)

    def test_negative(self):
        self.assertEqual(profit_amount(-1, 0), None)
        self.assertEqual(profit_amount(0, -1), None)
        self.assertEqual(profit_amount(-1, -2), 3)
