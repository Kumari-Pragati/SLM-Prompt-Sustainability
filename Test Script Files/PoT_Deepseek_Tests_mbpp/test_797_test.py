import unittest
from mbpp_797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_in_Range(1, 5), 10)
        self.assertEqual(sum_in_Range(10, 20), 110)
        self.assertEqual(sum_in_Range(100, 200), 10110)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_in_Range(1, 1), 1)
        self.assertEqual(sum_in_Range(1, 2), 4)
        self.assertEqual(sum_in_Range(0, 1), 1)
        self.assertEqual(sum_in_Range(0, 0), 0)

    def test_invalid_or_exceptional_inputs(self):
        with self.assertRaises(Exception):
            sum_in_Range(-1, 5)
        with self.assertRaises(Exception):
            sum_in_Range(5, -1)
        with self.assertRaises(Exception):
            sum_in_Range(-1, -1)
