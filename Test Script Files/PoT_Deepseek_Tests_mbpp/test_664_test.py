import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(average_Even(10), 6)
        self.assertEqual(average_Even(20), 16)

    def test_edge_cases(self):
        self.assertEqual(average_Even(2), 2)
        self.assertEqual(average_Even(0), 0)

    def test_boundary_conditions(self):
        self.assertEqual(average_Even(4), 4)
        self.assertEqual(average_Even(8), 8)

    def test_invalid_input(self):
        self.assertEqual(average_Even(3), "Invalid Input")
        self.assertEqual(average_Even(-2), "Invalid Input")
