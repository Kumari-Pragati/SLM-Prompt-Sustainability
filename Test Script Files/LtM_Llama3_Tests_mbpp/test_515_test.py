import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(modular_sum([1, 2, 3], 3, 5))

    def test_edge_n_m_equal(self):
        self.assertTrue(modular_sum([1], 1, 1))

    def test_edge_n_m_greater(self):
        self.assertTrue(modular_sum([1, 2], 2, 1))

    def test_edge_n_empty(self):
        self.assertFalse(modular_sum([], 1, 5))

    def test_edge_m_zero(self):
        self.assertFalse(modular_sum([1], 1, 0))

    def test_edge_m_one(self):
        self.assertTrue(modular_sum([1], 1, 1))

    def test_edge_arr_empty(self):
        self.assertFalse(modular_sum([], 1, 5))

    def test_edge_arr_single(self):
        self.assertFalse(modular_sum([1], 1, 5))

    def test_edge_arr_single_zero(self):
        self.assertFalse(modular_sum([0], 1, 5))

    def test_edge_arr_single_one(self):
        self.assertTrue(modular_sum([1], 1, 5))

    def test_edge_arr_single_max(self):
        self.assertTrue(modular_sum([4], 1, 5))

    def test_edge_arr_single_min(self):
        self.assertFalse(modular_sum([-1], 1, 5))

    def test_edge_arr_multiple(self):
        self.assertTrue(modular_sum([1, 2, 3], 3, 5))

    def test_edge_arr_multiple_zero(self):
        self.assertFalse(modular_sum([0, 1, 2], 3, 5))

    def test_edge_arr_multiple_one(self):
        self.assertTrue(modular_sum([1, 1, 1], 3, 5))

    def test_edge_arr_multiple_max(self):
        self.assertTrue(modular_sum([4, 4, 4], 3, 5))

    def test_edge_arr_multiple_min(self):
        self.assertFalse(modular_sum([-1, -1, -1], 3, 5))
