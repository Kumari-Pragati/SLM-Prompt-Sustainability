import unittest
from797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):

    def test_empty_range(self):
        self.assertEqual(sum_in_Range(0, 0), 0)

    def test_single_number_range(self):
        self.assertEqual(sum_in_Range(1, 1), 0)
        self.assertEqual(sum_in_Range(2, 2), 1)
        self.assertEqual(sum_in_Range(3, 3), 3)

    def test_small_range(self):
        self.assertEqual(sum_in_Range(1, 5), 8)

    def test_large_range(self):
        self.assertEqual(sum_in_Range(1, 100), 2499)
        self.assertEqual(sum_in_Range(101, 200), 14999)

    def test_negative_numbers(self):
        self.assertEqual(sum_in_Range(-1, 0), -1)
        self.assertEqual(sum_in_Range(-1, 1), 0)
        self.assertEqual(sum_in_Range(-1, 2), 1)

    def test_large_negative_numbers(self):
        self.assertEqual(sum_in_Range(-100, -1), 9999)
        self.assertEqual(sum_in_Range(-100, 0), -100)

    def test_end_of_range_is_odd(self):
        self.assertEqual(sum_in_Range(1, 3), 2)
        self.assertEqual(sum_in_Range(3, 5), 6)
        self.assertEqual(sum_in_Range(5, 7), 10)

    def test_start_of_range_is_odd(self):
        self.assertEqual(sum_in_Range(1, 3), 2)
        self.assertEqual(sum_in_Range(3, 5), 6)
        self.assertEqual(sum_in_Range(5, 7), 10)

    def test_start_and_end_of_range_are_odd(self):
        self.assertEqual(sum_in_Range(1, 3), 2)
        self.assertEqual(sum_in_Range(3, 5), 6)
        self.assertEqual(sum_in_Range(5, 7), 10)

    def test_negative_start_and_end_of_range_are_odd(self):
        self.assertEqual(sum_in_Range(-3, -1), -2)
        self.assertEqual(sum_in_Range(-1, -3), 2)
        self.assertEqual(sum_in_Range(-5, -3), -6)
