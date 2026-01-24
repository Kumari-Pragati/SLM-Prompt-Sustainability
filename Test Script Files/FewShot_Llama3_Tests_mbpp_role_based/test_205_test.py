import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(inversion_elements((1, 0, 1)), (~1, ~0, ~1))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(inversion_elements(()), ())

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(inversion_elements((1,)), (~1,))

    def test_edge_case_single_element_tuple_with_zero(self):
        self.assertEqual(inversion_elements((0,)), (~0,))

    def test_edge_case_single_element_tuple_with_negative(self):
        self.assertEqual(inversion_elements((-1,)), (~(-1),))

    def test_edge_case_single_element_tuple_with_positive(self):
        self.assertEqual(inversion_elements((1,)), (~1,))

    def test_edge_case_single_element_tuple_with_large_positive(self):
        self.assertEqual(inversion_elements((2**31 - 1,)), (~((2**31 - 1)),))

    def test_edge_case_single_element_tuple_with_large_negative(self):
        self.assertEqual(inversion_elements((-2**31,)), (~(-2**31),))
