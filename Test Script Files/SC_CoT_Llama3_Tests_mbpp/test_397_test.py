import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(median_numbers(5, 3, 2), 3)
        self.assertEqual(median_numbers(2, 5, 3), 3)
        self.assertEqual(median_numbers(3, 2, 5), 3)

    def test_edge_cases(self):
        self.assertEqual(median_numbers(5, 5, 2), 5)
        self.assertEqual(median_numbers(2, 2, 5), 2)
        self.assertEqual(median_numbers(5, 2, 2), 2)

    def test_special_cases(self):
        self.assertEqual(median_numbers(1, 2, 3), 2)
        self.assertEqual(median_numbers(3, 2, 1), 2)
        self.assertEqual(median_numbers(2, 1, 3), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            median_numbers('a', 2, 3)
        with self.assertRaises(TypeError):
            median_numbers(2, 'a', 3)
        with self.assertRaises(TypeError):
            median_numbers(2, 3, 'a')
