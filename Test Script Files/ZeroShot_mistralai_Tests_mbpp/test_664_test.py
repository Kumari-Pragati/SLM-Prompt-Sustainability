import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):

    def test_invalid_input(self):
        self.assertEqual(average_Even(1), "Invalid Input")
        self.assertEqual(average_Even(-1), "Invalid Input")
        self.assertEqual(average_Even(0), "Invalid Input")

    def test_single_even_number(self):
        self.assertEqual(average_Even(2), 2)
        self.assertEqual(average_Even(4), 4)
        self.assertEqual(average_Even(6), 6)

    def test_multiple_even_numbers(self):
        self.assertEqual(average_Even(8), 4)
        self.assertEqual(average_Even(10), 6)
        self.assertEqual(average_Even(12), 8)
        self.assertEqual(average_Even(14), 10)
        self.assertEqual(average_Even(16), 12)

    def test_odd_numbers(self):
        self.assertEqual(average_Even(3), "Invalid Input")
        self.assertEqual(average_Even(5), "Invalid Input")
        self.assertEqual(average_Even(7), "Invalid Input")
