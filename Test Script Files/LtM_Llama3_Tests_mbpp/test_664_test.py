import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(average_Even(4), 2)
        self.assertEqual(average_Even(6), 3)
        self.assertEqual(average_Even(8), 4)

    def test_invalid_input(self):
        self.assertEqual(average_Even(1), "Invalid Input")
        self.assertEqual(average_Even(3), "Invalid Input")
        self.assertEqual(average_Even(5), "Invalid Input")

    def test_edge_case(self):
        self.assertEqual(average_Even(2), 0)
        self.assertEqual(average_Even(4), 2)
        self.assertEqual(average_Even(6), 3)

    def test_zero_input(self):
        self.assertEqual(average_Even(0), 0)

    def test_negative_input(self):
        self.assertEqual(average_Even(-2), 0)
        self.assertEqual(average_Even(-4), 0)
        self.assertEqual(average_Even(-6), 0)
