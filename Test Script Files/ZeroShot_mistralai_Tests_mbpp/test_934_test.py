import unittest
from934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):

    def test_dealnnoy_num_base_cases(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)
        self.assertEqual(dealnnoy_num(1, 0), 1)
        self.assertEqual(dealnnoy_num(0, 1), 1)
        self.assertEqual(dealnnoy_num(1, 1), 2)
        self.assertEqual(dealnnoy_num(2, 1), 3)
        self.assertEqual(dealnnoy_num(1, 2), 3)

    def test_dealnnoy_num_small_values(self):
        self.assertEqual(dealnnoy_num(3, 2), 8)
        self.assertEqual(dealnnoy_num(4, 3), 19)
        self.assertEqual(dealnnoy_num(5, 4), 49)
        self.assertEqual(dealnnoy_num(6, 5), 121)

    def test_dealnnoy_num_large_values(self):
        self.assertEqual(dealnnoy_num(10, 9), 274)
        self.assertEqual(dealnnoy_num(20, 19), 10946)
        self.assertEqual(dealnnoy_num(30, 29), 68018)
        self.assertEqual(dealnnoy_num(40, 39), 463680)
