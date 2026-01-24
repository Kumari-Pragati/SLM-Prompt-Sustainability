import unittest
from mbpp_797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):

    def test_sum_in_range_positive_numbers(self):
        self.assertEqual(sum_in_Range(1, 5), 10)
        self.assertEqual(sum_in_Range(10, 20), 105)
        self.assertEqual(sum_in_Range(100, 200), 10010)

    def test_sum_in_range_negative_numbers(self):
        self.assertEqual(sum_in_Range(-5, 5), 10)
        self.assertEqual(sum_in_Range(-10, 10), 0)
        self.assertEqual(sum_in_Range(-100, 100), 0)

    def test_sum_in_range_boundary_values(self):
        self.assertEqual(sum_in_Range(0, 0), 0)
        self.assertEqual(sum_in_Range(1, 1), 1)
        self.assertEqual(sum_in_Range(1000, 1000), 1000)

    def test_sum_in_range_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_in_Range("1", 5)
        with self.assertRaises(TypeError):
            sum_in_Range(1, "5")
        with self.assertRaises(TypeError):
            sum_in_Range("1", "5")
