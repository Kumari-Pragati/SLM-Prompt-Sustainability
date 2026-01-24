import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(average_Even(10), 6)

    def test_edge_boundary_conditions(self):
        self.assertEqual(average_Even(2), 2)
        self.assertEqual(average_Even(0), 0)
        self.assertEqual(average_Even(-2), "Invalid Input")

    def test_more_complex_cases(self):
        self.assertEqual(average_Even(12), 8)
        self.assertEqual(average_Even(14), "Invalid Input")
