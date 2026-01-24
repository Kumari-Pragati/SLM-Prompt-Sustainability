import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):
    def test_average_even_positive_numbers(self):
        self.assertEqual(average_Even(6), 3)
        self.assertEqual(average_Even(10), 5)
        self.assertEqual(average_Even(14), 7)

    def test_average_even_zero(self):
        self.assertEqual(average_Even(0), 0)

    def test_average_even_negative_numbers(self):
        self.assertEqual(average_Even(-2), -1)
        self.assertEqual(average_Even(-6), -3)

    def test_average_even_single_number(self):
        self.assertEqual(average_Even(2), 1)
        self.assertEqual(average_Even(4), 2)

    def test_average_even_odd_number(self):
        self.assertEqual(average_Even(1), "Invalid Input")
        self.assertEqual(average_Even(3), "Invalid Input")
        self.assertEqual(average_Even(5), "Invalid Input")
