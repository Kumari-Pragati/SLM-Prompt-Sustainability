import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(median_numbers(1, 2, 3), 2)
        self.assertEqual(median_numbers(3, 2, 1), 2)
        self.assertEqual(median_numbers(2, 1, 3), 2)
        self.assertEqual(median_numbers(1, 1, 1), 1)

    def test_edge_cases(self):
        self.assertEqual(median_numbers(1, 1, 2), 1)
        self.assertEqual(median_numbers(2, 1, 1), 1)
        self.assertEqual(median_numbers(1, 2, 2), 2)
        self.assertEqual(median_numbers(2, 2, 1), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            median_numbers('a', 2, 3)
        with self.assertRaises(TypeError):
            median_numbers(1, 'b', 3)
        with self.assertRaises(TypeError):
            median_numbers(1, 2, 'c')
