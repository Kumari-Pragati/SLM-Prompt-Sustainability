import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(modular_inverse([2, 3, 5], 10, 7), 3)
        self.assertEqual(modular_inverse([7, 1], 10, 5), 4)
        self.assertEqual(modular_inverse([4, 6], 10, 5), 9)

    def test_edge_case_zero(self):
        self.assertEqual(modular_inverse([0], 10, 7), 0)

    def test_edge_case_one(self):
        self.assertEqual(modular_inverse([1], 10, 7), 1)

    def test_edge_case_negative(self):
        self.assertEqual(modular_inverse([-1], 10, 7), 6)

    def test_edge_case_empty(self):
        self.assertEqual(modular_inverse([], 10, 7), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(modular_inverse([2], 10, 7), 0)

    def test_edge_case_large_input(self):
        self.assertEqual(modular_inverse([2, 3, 4, 5, 6, 7, 8, 9], 10, 7), 3)

    def test_invalid_input_arr(self):
        self.assertRaises(TypeError, modular_inverse, "string", 10, 7)

    def test_invalid_input_N(self):
        self.assertRaises(TypeError, modular_inverse, [2, 3], "string", 7)

    def test_invalid_input_P(self):
        self.assertRaises(TypeError, modular_inverse, [2, 3], 10, "string")
