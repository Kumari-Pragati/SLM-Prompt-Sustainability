import unittest
from797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_in_Range(1, 5), 6)
        self.assertEqual(sum_in_Range(5, 10), 25)
        self.assertEqual(sum_in_Range(10, 15), 50)

    def test_edge_cases(self):
        self.assertEqual(sum_in_Range(0, 1), 0)
        self.assertEqual(sum_in_Range(1, 0), 0)
        self.assertEqual(sum_in_Range(1, 1), 0)
        self.assertEqual(sum_in_Range(5, 5), 0)

    def test_boundary_cases(self):
        self.assertEqual(sum_in_Range(-1, 1), 0)
        self.assertEqual(sum_in_Range(1, -1), 0)
        self.assertEqual(sum_in_Range(1, 2147483647), 1073741823)
        self.assertEqual(sum_in_Range(2147483647, 1), 1073741823)
