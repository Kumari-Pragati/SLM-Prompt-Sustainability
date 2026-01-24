import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(inversion_elements((1, 2, 3)), (~1, ~2, ~3))

    def test_edge_condition(self):
        self.assertEqual(inversion_elements((0,)), (~0,))

    def test_boundary_condition(self):
        self.assertEqual(inversion_elements((-1, 1)), (~-1, ~1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            inversion_elements("1, 2, 3")
