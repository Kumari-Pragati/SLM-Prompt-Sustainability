import unittest
from mbpp_934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):

    def test_zero_input(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)
        self.assertEqual(dealnnoy_num(0, 5), 1)
        self.assertEqual(dealnnoy_num(5, 0), 1)

    def test_typical_cases(self):
        self.assertEqual(dealnnoy_num(2, 2), 5)
        self.assertEqual(dealnnoy_num(3, 2), 9)
        self.assertEqual(dealnnoy_num(2, 3), 9)

    def test_large_numbers(self):
        self.assertEqual(dealnnoy_num(5, 5), 165)
        self.assertEqual(dealnnoy_num(10, 10), 167960)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            dealnnoy_num("2", 2)
        with self.assertRaises(TypeError):
            dealnnoy_num(2, "2")
        with self.assertRaises(TypeError):
            dealnnoy_num("2", "2")
        with self.assertRaises(ValueError):
            dealnnoy_num(-2, 2)
        with self.assertRaises(ValueError):
            dealnnoy_num(2, -2)
