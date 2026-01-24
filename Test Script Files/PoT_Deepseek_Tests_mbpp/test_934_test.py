import unittest
from mbpp_934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(dealnnoy_num(2, 2), 5)
        self.assertEqual(dealnnoy_num(3, 2), 13)
        self.assertEqual(dealnnoy_num(2, 3), 13)

    def test_edge_cases(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)
        self.assertEqual(dealnnoy_num(0, 1), 1)
        self.assertEqual(dealnnoy_num(1, 0), 1)

    def test_boundary_cases(self):
        self.assertEqual(dealnnoy_num(1, 1), 2)
        self.assertEqual(dealnnoy_num(2, 1), 4)
        self.assertEqual(dealnnoy_num(1, 2), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            dealnnoy_num(-1, 2)
        with self.assertRaises(Exception):
            dealnnoy_num(2, -1)
