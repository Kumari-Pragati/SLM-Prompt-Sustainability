import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(add_pairwise((1, 2, 3, 4)), (3, 4, 5, 6))

    def test_edge_case_single_element(self):
        self.assertEqual(add_pairwise((1,)), ())

    def test_edge_case_empty_input(self):
        self.assertEqual(add_pairwise(()), ())

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(add_pairwise((1,)), ())

    def test_edge_case_empty_input_tuple(self):
        self.assertEqual(add_pairwise(()), ())

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            add_pairwise(123)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            add_pairwise(("a", "b"))
