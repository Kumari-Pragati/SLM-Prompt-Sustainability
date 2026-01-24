import unittest
from mbpp_925_code import mutiple_tuple

class TestMultipleTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(mutiple_tuple([1, 2, 3]), 6)

    def test_edge_case_empty_list(self):
        self.assertEqual(mutiple_tuple([]), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(mutiple_tuple([1]), 1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(mutiple_tuple([-1, -2, -3]), 6)

    def test_corner_case_zero(self):
        self.assertEqual(mutiple_tuple([0]), 0)
