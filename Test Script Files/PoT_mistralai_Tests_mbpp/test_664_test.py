import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(average_Even(6), 4)
        self.assertEqual(average_Even(10), 6)
        self.assertEqual(average_Even(14), 8)

    def test_edge_cases(self):
        self.assertEqual(average_Even(0), -1)
        self.assertEqual(average_Even(1), -1)
        self.assertEqual(average_Even(2), 0)
        self.assertEqual(average_Even(3), "Invalid Input")

    def test_corner_cases(self):
        self.assertEqual(average_Even(4), 2)
        self.assertEqual(average_Even(5), "Invalid Input")
        self.assertEqual(average_Even(6), 4)
        self.assertEqual(average_Even(7), "Invalid Input")
