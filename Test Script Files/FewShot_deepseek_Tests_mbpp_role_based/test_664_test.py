import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(average_Even(10), 7)

    def test_boundary_conditions(self):
        self.assertEqual(average_Even(2), 2)
        self.assertEqual(average_Even(0), 0)

    def test_edge_cases(self):
        self.assertEqual(average_Even(1), "Invalid Input")
        self.assertEqual(average_Even(-2), "Invalid Input")

    def test_invalid_inputs(self):
        self.assertEqual(average_Even("abc"), "Invalid Input")
        self.assertEqual(average_Even(None), "Invalid Input")
        self.assertEqual(average_Even([1, 2, 3]), "Invalid Input")
