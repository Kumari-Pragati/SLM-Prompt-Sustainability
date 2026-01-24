import unittest
from mbpp_934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(dealnnoy_num(1, 2), 3)
        self.assertEqual(dealnnoy_num(2, 2), 4)
        self.assertEqual(dealnnoy_num(3, 2), 10)
        self.assertEqual(dealnnoy_num(4, 2), 20)
        self.assertEqual(dealnnoy_num(5, 2), 35)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)
        self.assertEqual(dealnnoy_num(0, 1), 1)
        self.assertEqual(dealnnoy_num(1, 0), 1)
        self.assertEqual(dealnnoy_num(1, 1), 1)
        self.assertEqual(dealnnoy_num(2, 0), 1)
        self.assertEqual(dealnnoy_num(0, 2), 1)
