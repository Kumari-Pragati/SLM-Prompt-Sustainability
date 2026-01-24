import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):

    def test_simple_positive_numbers(self):
        self.assertEqual(inversion_elements((1, 2, 3)), (~1, ~2, ~3))

    def test_simple_negative_numbers(self):
        self.assertEqual(inversion_elements((-1, -2, -3)), (~-1, ~-2, ~-3))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(inversion_elements(()), ())

    def test_boundary_case_single_element(self):
        self.assertEqual(inversion_elements((1,)), (~1,))

    def test_complex_case_mixed_positive_negative(self):
        self.assertEqual(inversion_elements((1, -2, 3, -4)), (~1, ~-2, ~3, ~-4))

    def test_boundary_case_maximum_minimum_values(self):
        self.assertEqual(inversion_elements((-128, 127)), (~-128, ~127))
