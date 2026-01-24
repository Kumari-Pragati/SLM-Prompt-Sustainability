import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(average_Even(10), 5)
        self.assertEqual(average_Even(12), 6)
        self.assertEqual(average_Even(14), 7)

    def test_invalid_input(self):
        self.assertEqual(average_Even(1), "Invalid Input")
        self.assertEqual(average_Even(3), "Invalid Input")
        self.assertEqual(average_Even(5), "Invalid Input")

    def test_zero_input(self):
        self.assertEqual(average_Even(0), 0)

    def test_negative_input(self):
        self.assertEqual(average_Even(-10), "Invalid Input")
        self.assertEqual(average_Even(-12), "Invalid Input")
        self.assertEqual(average_Even(-14), "Invalid Input")

    def test_edge_case(self):
        self.assertEqual(average_Even(2), 1)
        self.assertEqual(average_Even(4), 2)
        self.assertEqual(average_Even(6), 3)
