import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(average_Even(10), 5)

    def test_zero(self):
        self.assertEqual(average_Even(0), 0)

    def test_single_even_number(self):
        self.assertEqual(average_Even(2), 2)

    def test_multiple_even_numbers(self):
        self.assertEqual(average_Even(4), 2)

    def test_invalid_input(self):
        self.assertEqual(average_Even(1), "Invalid Input")
