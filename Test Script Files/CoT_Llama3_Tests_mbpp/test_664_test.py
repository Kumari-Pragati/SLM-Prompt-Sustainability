import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(average_Even(10), 5)

    def test_invalid_input(self):
        self.assertEqual(average_Even(5), "Invalid Input")

    def test_zero_input(self):
        self.assertEqual(average_Even(0), 0)

    def test_single_even_number(self):
        self.assertEqual(average_Even(4), 2)

    def test_multiple_even_numbers(self):
        self.assertEqual(average_Even(12), 6)

    def test_edge_case(self):
        self.assertEqual(average_Even(2), 1)

    def test_edge_case2(self):
        self.assertEqual(average_Even(4), 2)

    def test_edge_case3(self):
        self.assertEqual(average_Even(6), 3)
