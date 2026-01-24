import unittest
from mbpp_797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(sum_in_Range(1, 2), 1)
        self.assertEqual(sum_in_Range(2, 3), 2)
        self.assertEqual(sum_in_Range(3, 4), 3)

    def test_edge_cases(self):
        self.assertEqual(sum_in_Range(0, 0), 0)
        self.assertEqual(sum_in_Range(1, 1), 0)
        self.assertEqual(sum_in_Range(2, 2), 1)

    def test_negative_range(self):
        self.assertEqual(sum_in_Range(-1, 0), -1)
        self.assertEqual(sum_in_Range(-2, -1), -1)
        self.assertEqual(sum_in_Range(-3, -2), -2)

    def test_large_range(self):
        self.assertEqual(sum_in_Range(100, 200), 10000)
        self.assertEqual(sum_in_Range(200, 300), 20000)
        self.assertEqual(sum_in_Range(300, 400), 30000)
