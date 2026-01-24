import unittest
from mbpp_934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(dealnnoy_num(2, 3), 7)

    def test_edge_case_m_zero(self):
        self.assertEqual(dealnnoy_num(0, 3), 1)

    def test_edge_case_n_zero(self):
        self.assertEqual(dealnnoy_num(2, 0), 1)

    def test_edge_case_m_n_zero(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)

    def test_edge_case_m_one(self):
        self.assertEqual(dealnnoy_num(1, 3), 4)

    def test_edge_case_n_one(self):
        self.assertEqual(dealnnoy_num(2, 1), 3)

    def test_edge_case_m_n_one(self):
        self.assertEqual(dealnnoy_num(1, 1), 2)

    def test_invalid_input_m_negative(self):
        with self.assertRaises(TypeError):
            dealnnoy_num(-1, 3)

    def test_invalid_input_n_negative(self):
        with self.assertRaises(TypeError):
            dealnnoy_num(2, -1)

    def test_invalid_input_m_n_negative(self):
        with self.assertRaises(TypeError):
            dealnnoy_num(-1, -1)
