import unittest
from mbpp_934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(dealnnoy_num(2, 2), 5)

    def test_boundary_conditions(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)
        self.assertEqual(dealnnoy_num(0, 1), 1)
        self.assertEqual(dealnnoy_num(1, 0), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            dealnnoy_num('a', 1)
        with self.assertRaises(TypeError):
            dealnnoy_num(1, 'b')
        with self.assertRaises(TypeError):
            dealnnoy_num('a', 'b')
