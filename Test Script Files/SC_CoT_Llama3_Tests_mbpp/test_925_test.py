import unittest
from mbpp_925_code import mutiple_tuple

class TestMultipleTuple(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(mutiple_tuple((1, 2, 3)), 6)

    def test_edge_case_zero(self):
        self.assertEqual(mutiple_tuple((0, 1, 2)), 0)

    def test_edge_case_negative(self):
        self.assertEqual(mutiple_tuple((-1, 2, 3)), -6)

    def test_edge_case_single_element(self):
        self.assertEqual(mutiple_tuple((1,)), 1)

    def test_edge_case_empty(self):
        self.assertEqual(mutiple_tuple(()), 1)

    def test_edge_case_single_zero(self):
        self.assertEqual(mutiple_tuple((0,)), 0)

    def test_edge_case_single_negative(self):
        self.assertEqual(mutiple_tuple((-1,)), -1)

    def test_edge_case_multiple_zeros(self):
        self.assertEqual(mutiple_tuple((0, 0, 0)), 0)

    def test_edge_case_multiple_negatives(self):
        self.assertEqual(mutiple_tuple((-1, -2, -3)), -6)

    def test_edge_case_mixed(self):
        self.assertEqual(mutiple_tuple((1, 2, -3)), -6)

    def test_edge_case_mixed_zeros(self):
        self.assertEqual(mutiple_tuple((1, 2, 0, -3)), 0)

    def test_edge_case_mixed_negatives(self):
        self.assertEqual(mutiple_tuple((1, 2, -1, -3)), -6)
