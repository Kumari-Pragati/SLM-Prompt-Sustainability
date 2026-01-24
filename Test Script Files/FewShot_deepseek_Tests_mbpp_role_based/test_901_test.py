import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(smallest_multiple(10), 20)

    def test_edge_case(self):
        self.assertEqual(smallest_multiple(2), 2)

    def test_boundary_case(self):
        self.assertEqual(smallest_multiple(1), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            smallest_multiple('a')

    def test_zero_input(self):
        with self.assertRaises(ValueError):
            smallest_multiple(0)
