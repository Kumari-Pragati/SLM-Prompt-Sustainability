import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(add_pairwise((1, 2, 3, 4)), (2, 3, 4))

    def test_edge_case_empty_list(self):
        self.assertEqual(add_pairwise([]), ())

    def test_edge_case_single_element(self):
        self.assertEqual(add_pairwise((1,)), (1,))

    def test_edge_case_single_element_right(self):
        self.assertEqual(add_pairwise((1,), (2,)), (2,))

    def test_boundary_case_first_zero(self):
        self.assertEqual(add_pairwise((0, 1, 2, 3)), (1, 2, 3))

    def test_boundary_case_last_zero(self):
        self.assertEqual(add_pairwise((1, 2, 3, 0)), (1, 2, 3))
