import unittest
from mbpp_925_code import mutiple_tuple

class TestMutipleTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(mutiple_tuple((1, 2, 3)), 6)

    def test_edge_case_zero(self):
        self.assertEqual(mutiple_tuple((0, 1, 2)), 0)

    def test_edge_case_negative(self):
        self.assertEqual(mutiple_tuple((-1, 2, 3)), -6)

    def test_edge_case_single_element(self):
        self.assertEqual(mutiple_tuple((5)), 5)

    def test_edge_case_empty(self):
        self.assertEqual(mutiple_tuple(()), 1)

    def test_edge_case_single_zero(self):
        self.assertEqual(mutiple_tuple((0)), 0)

    def test_edge_case_single_negative(self):
        self.assertEqual(mutiple_tuple((-1)), -1)

    def test_edge_case_multiple_zeros(self):
        self.assertEqual(mutiple_tuple((0, 0, 0)), 0)

    def test_edge_case_multiple_negatives(self):
        self.assertEqual(mutiple_tuple((-1, -2, -3)), -6)

    def test_edge_case_mixed(self):
        self.assertEqual(mutiple_tuple((1, 2, 0, -1)), 0)
