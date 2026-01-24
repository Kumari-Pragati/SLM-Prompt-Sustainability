import unittest
from mbpp_797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):
    def test_sum_in_range(self):
        self.assertEqual(sum_in_Range(1, 3), 2)
        self.assertEqual(sum_in_Range(2, 4), 3)
        self.assertEqual(sum_in_Range(5, 7), 9)
        self.assertEqual(sum_in_Range(10, 12), 15)
        self.assertEqual(sum_in_Range(-1, 1), 1)
        self.assertEqual(sum_in_Range(-5, 5), 15)
        self.assertEqual(sum_in_Range(-10, 10), 25)

    def test_sum_in_range_edge_cases(self):
        self.assertEqual(sum_in_Range(1, 1), 0)
        self.assertEqual(sum_in_Range(-1, -1), 0)
        self.assertEqual(sum_in_Range(1, 1), 0)

    def test_sum_in_range_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_in_Range('a', 2)
        with self.assertRaises(TypeError):
            sum_in_Range(1, 'b')
