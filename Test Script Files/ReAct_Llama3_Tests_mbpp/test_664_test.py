import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(average_Even(4), 2)

    def test_invalid_input(self):
        self.assertEqual(average_Even(3), "Invalid Input")

    def test_zero_input(self):
        self.assertEqual(average_Even(0), 0)

    def test_single_even_input(self):
        self.assertEqual(average_Even(2), 2)

    def test_multiple_even_input(self):
        self.assertEqual(average_Even(8), 4)

    def test_multiple_even_input_with_zero(self):
        self.assertEqual(average_Even(10), 5)

    def test_edge_case_input(self):
        self.assertEqual(average_Even(2), 2)

    def test_edge_case_input_with_zero(self):
        self.assertEqual(average_Even(0), 0)
