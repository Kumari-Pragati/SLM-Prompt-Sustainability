import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(lobb_num(1, 1), 2)

    def test_edge_case_n_zero(self):
        self.assertEqual(lobb_num(0, 1), 1)

    def test_edge_case_m_zero(self):
        self.assertEqual(lobb_num(1, 0), 1)

    def test_edge_case_n_and_m_zero(self):
        self.assertEqual(lobb_num(0, 0), 1)

    def test_edge_case_m_greater_than_n(self):
        self.assertEqual(lobb_num(1, 2), 2)

    def test_edge_case_n_greater_than_m(self):
        self.assertEqual(lobb_num(2, 1), 2)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            lobb_num('a', 1)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            lobb_num(1, 'a')

    def test_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            lobb_num('a', 'b')
