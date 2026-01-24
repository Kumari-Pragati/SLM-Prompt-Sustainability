import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(median_numbers(1, 2, 3), 2)

    def test_edge_case(self):
        self.assertEqual(median_numbers(1, 1, 1), 1)

    def test_boundary_case(self):
        self.assertEqual(median_numbers(0, 0, 0), 0)
        self.assertEqual(median_numbers(1000000, 1000000, 1000000), 1000000)

    def test_corner_case(self):
        self.assertEqual(median_numbers(-1, -2, -3), -2)
        self.assertEqual(median_numbers(0.5, 0.4, 0.6), 0.5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            median_numbers(1, '2', 3)
        with self.assertRaises(TypeError):
            median_numbers(1, 2, None)
