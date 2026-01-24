import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(swap_numbers(1, 2), (2, 1))

    def test_boundary_case(self):
        self.assertEqual(swap_numbers(0, 0), (0, 0))

    def test_edge_case(self):
        self.assertEqual(swap_numbers(-1, 1), (1, -1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            swap_numbers("a", 1)
