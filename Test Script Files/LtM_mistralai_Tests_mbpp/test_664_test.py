import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):

    def test_simple_even_input(self):
        self.assertEqual(average_Even(6), 4)
        self.assertEqual(average_Even(10), 6)

    def test_simple_odd_input(self):
        self.assertEqual(average_Even(1), "Invalid Input")
        self.assertEqual(average_Even(3), "Invalid Input")

    def test_edge_cases(self):
        self.assertEqual(average_Even(0), "Invalid Input")
        self.assertEqual(average_Even(2), 2)
        self.assertEqual(average_Even(4), 2)

    def test_boundary_cases(self):
        self.assertEqual(average_Even(14), 8)
        self.assertEqual(average_Even(26), 12)

    def test_negative_input(self):
        self.assertEqual(average_Even(-1), "Invalid Input")

    def test_large_input(self):
        self.assertEqual(average_Even(100000), 50000)
