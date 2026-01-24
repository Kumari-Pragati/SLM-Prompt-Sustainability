import unittest
from mbpp_934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(dealnnoy_num(2, 2), 4)
        self.assertEqual(dealnnoy_num(3, 3), 13)
        self.assertEqual(dealnnoy_num(4, 4), 49)

    def test_edge_cases(self):
        self.assertEqual(dealnnoy_num(0, 2), 1)
        self.assertEqual(dealnnoy_num(2, 0), 1)
        self.assertEqual(dealnnoy_num(1, 0), 1)
        self.assertEqual(dealnnoy_num(0, 0), 1)

    def test_boundary_cases(self):
        self.assertEqual(dealnnoy_num(1, 1), 2)
        self.assertEqual(dealnnoy_num(2, 1), 3)
        self.assertEqual(dealnnoy_num(1, 2), 3)
