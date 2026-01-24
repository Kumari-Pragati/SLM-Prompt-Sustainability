import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):

    def test_smallest_multiple_typical_case(self):
        self.assertEqual(smallest_multiple(5), 20)

    def test_smallest_multiple_edge_case(self):
        self.assertEqual(smallest_multiple(2), 2)

    def test_smallest_multiple_boundary_case(self):
        self.assertEqual(smallest_multiple(1), 1)

    def test_smallest_multiple_invalid_input(self):
        with self.assertRaises(TypeError):
            smallest_multiple('a')

        with self.assertRaises(ValueError):
            smallest_multiple(0)

        with self.assertRaises(ValueError):
            smallest_multiple(-1)
