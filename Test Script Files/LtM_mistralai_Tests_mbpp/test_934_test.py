import unittest
from mbpp_934_code import dealnnoy_num

class TestDealNnoyNum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(dealnnoy_num(1, 1), 1)
        self.assertEqual(dealnnoy_num(2, 2), 3)
        self.assertEqual(dealnnoy_num(3, 3), 7)

    def test_edge_cases(self):
        self.assertEqual(dealnnoy_num(0, 1), 1)
        self.assertEqual(dealnnoy_num(1, 0), 1)
        self.assertEqual(dealnnoy_num(0, 0), 1)

    def test_boundary_conditions(self):
        self.assertEqual(dealnnoy_num(1, 0), 0)
        self.assertEqual(dealnnoy_num(0, 1), 0)
        self.assertEqual(dealnnoy_num(1, 1000), 1000)
        self.assertEqual(dealnnoy_num(1000, 1), 1000)
