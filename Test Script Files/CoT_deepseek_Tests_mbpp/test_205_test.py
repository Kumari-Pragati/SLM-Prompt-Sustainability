import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(inversion_elements((1, 2, 3)), (~1, ~2, ~3))

    def test_empty_tuple(self):
        self.assertEqual(inversion_elements(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(inversion_elements((42,)), (~42,))

    def test_negative_numbers(self):
        self.assertEqual(inversion_elements((-1, -2, -3)), (~-1, ~-2, ~-3))

    def test_large_numbers(self):
        self.assertEqual(inversion_elements((1000, 2000, 3000)), (~1000, ~2000, ~3000))

    def test_mixed_numbers(self):
        self.assertEqual(inversion_elements((1, -2, 3)), (~1, ~-2, ~3))

    def test_float_numbers(self):
        self.assertEqual(inversion_elements((1.5, 2.5, 3.5)), (~1.5, ~2.5, ~3.5))

    def test_string_elements(self):
        with self.assertRaises(TypeError):
            inversion_elements(('a', 'b', 'c'))

    def test_list_elements(self):
        with self.assertRaises(TypeError):
            inversion_elements([1, 2, 3])

    def test_none_elements(self):
        with self.assertRaises(TypeError):
            inversion_elements((None,))
