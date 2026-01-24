import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(average_Even(6), 4)
        self.assertEqual(average_Even(10), 6)
        self.assertEqual(average_Even(14), 8)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(average_Even(0), -1)
        self.assertEqual(average_Even(1), -1)
        self.assertEqual(average_Even(2), 0)
        self.assertEqual(average_Even(3), -1)
        self.assertEqual(average_Even(4), 2)
        self.assertEqual(average_Even(5), -1)

    def test_invalid_input(self):
        self.assertEqual(average_Even(-1), "Invalid Input")
        self.assertEqual(average_Even(float('inf')), "Invalid Input")
        self.assertEqual(average_Even(complex(0, 1)), "Invalid Input")
        self.assertEqual(average_Even('hello'), "Invalid Input")
