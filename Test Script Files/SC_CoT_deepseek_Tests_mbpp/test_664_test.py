import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(average_Even(10), 7)

    def test_edge_case(self):
        self.assertEqual(average_Even(2), 2)

    def test_boundary_case(self):
        self.assertEqual(average_Even(0), 0)
        self.assertEqual(average_Even(-2), "Invalid Input")

    def test_special_case(self):
        self.assertEqual(average_Even(4), 4)
        self.assertEqual(average_Even(6), 5)

    def test_invalid_input(self):
        self.assertEqual(average_Even(3), "Invalid Input")
        self.assertEqual(average_Even(-1), "Invalid Input")
        self.assertEqual(average_Even(1.5), "Invalid Input")
        self.assertEqual(average_Even("2"), "Invalid Input")
