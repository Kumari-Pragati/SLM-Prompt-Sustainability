import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):

    def test_simple_case_1(self):
        self.assertEqual(median_numbers(1, 2, 3), 2)

    def test_simple_case_2(self):
        self.assertEqual(median_numbers(3, 2, 1), 2)

    def test_simple_case_3(self):
        self.assertEqual(median_numbers(2, 3, 1), 2)

    def test_edge_case_1(self):
        self.assertEqual(median_numbers(float('-inf'), 2, 1), 2)

    def test_edge_case_2(self):
        self.assertEqual(median_numbers(1, float('inf'), 2), 1)

    def test_edge_case_3(self):
        self.assertEqual(median_numbers(1, 2, float('inf')), 1)

    def test_edge_case_4(self):
        self.assertEqual(median_numbers(float('-inf'), 1, 2), -float('inf'))

    def test_edge_case_5(self):
        self.assertEqual(median_numbers(1, float('-inf'), 2), 1)

    def test_edge_case_6(self):
        self.assertEqual(median_numbers(float('-inf'), 1, float('-inf')), float('-inf'))

    def test_edge_case_7(self):
        self.assertEqual(median_numbers(1, float('inf'), float('inf')), 1)

    def test_complex_case_1(self):
        self.assertEqual(median_numbers(float('-inf'), 0, float('inf')), 0)
