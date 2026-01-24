import unittest
from mbpp_934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):
    def test_zero_input(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)

    def test_zero_m(self):
        self.assertEqual(dealnnoy_num(1, 0), 1)

    def test_zero_n(self):
        self.assertEqual(dealnnoy_num(0, 1), 1)

    def test_nonzero_input(self):
        self.assertEqual(dealnnoy_num(2, 2), 7)

    def test_edge_case_m(self):
        self.assertEqual(dealnnoy_num(1, 1), 2)

    def test_edge_case_n(self):
        self.assertEqual(dealnnoy_num(2, 1), 3)

    def test_invalid_input(self):
        with self.assertRaises RecursionError:
            dealnnoy_num(1000, 1000)
