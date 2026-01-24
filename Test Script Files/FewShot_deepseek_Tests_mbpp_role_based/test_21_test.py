import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(multiples_of_num(3, 5), [5, 10, 15])

    def test_edge_case_m_equals_zero(self):
        self.assertEqual(multiples_of_num(0, 5), [])

    def test_boundary_case_m_equals_one(self):
        self.assertEqual(multiples_of_num(1, 5), [5])

    def test_boundary_case_n_equals_one(self):
        self.assertEqual(multiples_of_num(3, 1), [1, 2, 3])

    def test_invalid_input_n_less_than_one(self):
        with self.assertRaises(ValueError):
            multiples_of_num(3, 0)

    def test_invalid_input_m_less_than_one(self):
        with self.assertRaises(ValueError):
            multiples_of_num(0, 5)
