import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(inversion_elements((1, 2, 3)), (~1, ~2, ~3))

    def test_empty_tuple(self):
        self.assertEqual(inversion_elements(()), ())

    def test_single_element(self):
        self.assertEqual(inversion_elements((10,)), (~10,))

    def test_negative_numbers(self):
        self.assertEqual(inversion_elements((-1, -2, -3)), (~-1, ~-2, ~-3))

    def test_large_numbers(self):
        self.assertEqual(inversion_elements((10000, 20000, 30000)), (~10000, ~20000, ~30000))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            inversion_elements("1,2,3")
