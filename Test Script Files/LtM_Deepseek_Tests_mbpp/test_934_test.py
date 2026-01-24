import unittest
from mbpp_934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(dealnnoy_num(1, 1), 1)
        self.assertEqual(dealnnoy_num(2, 2), 2)
        self.assertEqual(dealnnoy_num(3, 2), 4)

    def test_edge_conditions(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)
        self.assertEqual(dealnnoy_num(0, 1), 1)
        self.assertEqual(dealnnoy_num(1, 0), 1)

    def test_boundary_conditions(self):
        self.assertEqual(dealnnoy_num(10, 10), 1024)
        self.assertEqual(dealnnoy_num(20, 20), 1048576)

    def test_complex_cases(self):
        self.assertEqual(dealnnoy_num(5, 3), 21)
        self.assertEqual(dealnnoy_num(7, 4), 141)
