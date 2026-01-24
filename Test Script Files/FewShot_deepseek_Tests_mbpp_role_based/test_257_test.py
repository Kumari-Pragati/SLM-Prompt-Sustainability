import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(swap_numbers(1, 2), (2, 1))

    def test_boundary_conditions(self):
        self.assertEqual(swap_numbers(0, 0), (0, 0))
        self.assertEqual(swap_numbers(-1, -2), (-2, -1))

    def test_large_numbers(self):
        self.assertEqual(swap_numbers(1000000, 2000000), (2000000, 1000000))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            swap_numbers("a", 1)
        with self.assertRaises(TypeError):
            swap_numbers(1, "b")
        with self.assertRaises(TypeError):
            swap_numbers("a", "b")
