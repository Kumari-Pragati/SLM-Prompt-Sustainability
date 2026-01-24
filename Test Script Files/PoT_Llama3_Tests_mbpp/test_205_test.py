import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(inversion_elements((1, 2, 3)), (~1, ~2, ~3))

    def test_edge_case_zero(self):
        self.assertEqual(inversion_elements((0,)), (~0,))

    def test_edge_case_negative(self):
        self.assertEqual(inversion_elements((-1, -2, -3)), (~(-1), ~(-2), ~(-3)))

    def test_edge_case_positive(self):
        self.assertEqual(inversion_elements((1, 2, 3)), (~1, ~2, ~3))

    def test_edge_case_mixed(self):
        self.assertEqual(inversion_elements((-1, 2, -3)), (~(-1), ~2, ~(-3)))

    def test_edge_case_empty(self):
        self.assertEqual(inversion_elements(()), ())

    def test_edge_case_single(self):
        self.assertEqual(inversion_elements((1,)), (~1,))

    def test_edge_case_single_zero(self):
        self.assertEqual(inversion_elements((0,)), (~0,))

    def test_edge_case_single_negative(self):
        self.assertEqual(inversion_elements((-1,)), (~(-1),))

    def test_edge_case_single_positive(self):
        self.assertEqual(inversion_elements((1,)), (~1,))
