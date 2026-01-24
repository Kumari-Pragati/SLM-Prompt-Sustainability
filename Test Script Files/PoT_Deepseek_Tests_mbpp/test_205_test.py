import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(inversion_elements((1, 2, 3)), (~1, ~2, ~3))

    def test_empty_tuple(self):
        self.assertEqual(inversion_elements(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(inversion_elements((5,)), (~5,))

    def test_negative_numbers(self):
        self.assertEqual(inversion_elements((-1, -2, -3)), (~-1, ~-2, ~-3))

    def test_zero(self):
        self.assertEqual(inversion_elements((0,)), (0,))

    def test_large_numbers(self):
        self.assertEqual(inversion_elements((1000, 2000, 3000)), (~1000, ~2000, ~3000))

    def test_mixed_numbers(self):
        self.assertEqual(inversion_elements((1, -2, 3)), (~1, ~-2, ~3))
