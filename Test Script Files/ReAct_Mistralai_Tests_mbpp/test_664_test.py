import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(average_Even(0), -1, "Invalid input for empty list")

    def test_odd_number(self):
        self.assertEqual(average_Even(1), "Invalid Input")
        self.assertEqual(average_Even(3), "Invalid Input")

    def test_single_even_number(self):
        self.assertEqual(average_Even(2), 2)
        self.assertEqual(average_Even(4), 4)
        self.assertEqual(average_Even(6), 6)

    def test_multiple_even_numbers(self):
        self.assertEqual(average_Even(8), 4)
        self.assertEqual(average_Even(10), 6)
        self.assertEqual(average_Even(12), 8)
        self.assertEqual(average_Even(14), 10)

    def test_large_even_numbers(self):
        self.assertEqual(average_Even(100), 50)
        self.assertEqual(average_Even(200), 100)
        self.assertEqual(average_Even(400), 200)

    def test_negative_even_numbers(self):
        self.assertEqual(average_Even(-2), 1)
        self.assertEqual(average_Even(-4), 2)
        self.assertEqual(average_Even(-6), 3)
