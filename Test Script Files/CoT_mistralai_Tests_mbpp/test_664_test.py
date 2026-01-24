import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):
    def test_average_even_positive_numbers(self):
        self.assertEqual(average_Even(6), 4)
        self.assertEqual(average_Even(10), 6)
        self.assertEqual(average_Even(14), 8)

    def test_average_even_zero(self):
        self.assertEqual(average_Even(0), 0)

    def test_average_even_negative_numbers(self):
        self.assertEqual(average_Even(-2), -1)
        self.assertEqual(average_Even(-6), -3)
        self.assertEqual(average_Even(-10), -5)

    def test_average_even_odd_numbers(self):
        self.assertEqual(average_Even(1), "Invalid Input")
        self.assertEqual(average_Even(3), "Invalid Input")
        self.assertEqual(average_Even(5), "Invalid Input")

    def test_average_even_small_numbers(self):
        self.assertEqual(average_Even(2), 2)
        self.assertEqual(average_Even(4), 2)
