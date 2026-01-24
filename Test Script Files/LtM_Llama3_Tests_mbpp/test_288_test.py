import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(modular_inverse([1, 2, 3], 3, 5), 1)

    def test_edge_case_empty_input(self):
        self.assertEqual(modular_inverse([], 3, 5), 0)

    def test_edge_case_single_element_input(self):
        self.assertEqual(modular_inverse([1], 1, 5), 1)

    def test_edge_case_N_is_zero(self):
        self.assertEqual(modular_inverse([1, 2, 3], 0, 5), 0)

    def test_edge_case_P_is_one(self):
        self.assertEqual(modular_inverse([1, 2, 3], 3, 1), 0)

    def test_edge_case_P_is_zero(self):
        self.assertEqual(modular_inverse([1, 2, 3], 3, 0), 0)

    def test_edge_case_N_is_one(self):
        self.assertEqual(modular_inverse([1], 1, 5), 1)

    def test_edge_case_N_is_greater_than_P(self):
        self.assertEqual(modular_inverse([1, 2, 3], 5, 5), 0)

    def test_edge_case_N_is_equal_to_P(self):
        self.assertEqual(modular_inverse([1, 2, 3], 5, 5), 0)
