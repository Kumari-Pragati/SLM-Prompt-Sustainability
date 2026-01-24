import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):

    def test_average_Even_with_even_number(self):
        self.assertEqual(average_Even(100), 50)
        self.assertEqual(average_Even(4), 2)
        self.assertEqual(average_Even(10000), 5000)

    def test_average_Even_with_odd_number(self):
        self.assertEqual(average_Even(99), "Invalid Input")
        self.assertEqual(average_Even(1), "Invalid Input")
        self.assertEqual(average_Even(0), "Invalid Input")

    def test_average_Even_with_negative_number(self):
        self.assertEqual(average_Even(-100), "Invalid Input")
        self.assertEqual(average_Even(-1), "Invalid Input")
        self.assertEqual(average_Even(-10000), "Invalid Input")
