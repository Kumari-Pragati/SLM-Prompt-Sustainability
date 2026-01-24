import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(average_Even(10), 5)

    def test_edge_case_zero(self):
        self.assertEqual(average_Even(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(average_Even(2), 1)

    def test_edge_case_negative(self):
        self.assertEqual(average_Even(-4), -2)

    def test_edge_case_invalid(self):
        self.assertEqual(average_Even(1), "Invalid Input")

    def test_edge_case_zero_count(self):
        self.assertEqual(average_Even(4), 2)

    def test_edge_case_zero_sum(self):
        self.assertEqual(average_Even(6), 3)

    def test_edge_case_zero_input(self):
        self.assertEqual(average_Even(0), 0)

    def test_edge_case_negative_input(self):
        self.assertEqual(average_Even(-2), -1)
