import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(inversion_elements((1, 2, 3)), (~1, ~2, ~3))

    def test_empty_input(self):
        self.assertEqual(inversion_elements(()), ())

    def test_single_element_input(self):
        self.assertEqual(inversion_elements((5,)), (~5,))

    def test_negative_input(self):
        self.assertEqual(inversion_elements((-1, -2, -3)), (~(-1), ~(-2), ~(-3)))

    def test_mixed_input(self):
        self.assertEqual(inversion_elements((-1, 2, 3)), (~(-1), ~2, ~3))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            inversion_elements(("a", "b", "c"))
