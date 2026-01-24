import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(inversion_elements((1, 0, 1)), (~1, ~0, ~1))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(inversion_elements(()), ())

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(inversion_elements((1,)), (~1,))

    def test_edge_case_negative_numbers(self):
        self.assertEqual(inversion_elements((-1, -0, -1)), (~(-1), ~(-0), ~(-1)))

    def test_edge_case_zero(self):
        self.assertEqual(inversion_elements((0,)), (~0,))

    def test_edge_case_large_numbers(self):
        self.assertEqual(inversion_elements((100, 0, -100)), (~100, ~0, ~(-100)))

    def test_edge_case_mixed_signs(self):
        self.assertEqual(inversion_elements((-1, 0, 1)), (~(-1), ~0, ~1))

    def test_edge_case_mixed_types(self):
        self.assertEqual(inversion_elements((1, 0.0, -1)), (~1, ~0.0, ~(-1)))

    def test_edge_case_non_integer_types(self):
        self.assertEqual(inversion_elements((1.0, 0.0, -1.0)), (~1.0, ~0.0, ~(-1.0)))

    def test_edge_case_non_numeric_types(self):
        with self.assertRaises(TypeError):
            inversion_elements(("a", "b", "c"))
