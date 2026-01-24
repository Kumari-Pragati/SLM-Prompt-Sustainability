import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(median_numbers(1, 2, 3), 2)

    def test_edge_case(self):
        self.assertEqual(median_numbers(1, 1, 1), 1)

    def test_boundary_case(self):
        self.assertEqual(median_numbers(1, 2, 2), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            median_numbers("1", 2, 3)
