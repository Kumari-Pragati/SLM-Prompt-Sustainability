import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(compute_Last_Digit(1, 1), 1)
        self.assertEqual(compute_Last_Digit(2, 2), 1)
        self.assertEqual(compute_Last_Digit(3, 3), 1)
        self.assertEqual(compute_Last_Digit(4, 4), 1)
        self.assertEqual(compute_Last_Digit(5, 5), 1)
        self.assertEqual(compute_Last_Digit(6, 6), 1)
        self.assertEqual(compute_Last_Digit(7, 7), 1)
        self.assertEqual(compute_Last_Digit(8, 8), 1)
        self.assertEqual(compute_Last_Digit(9, 9), 1)
        self.assertEqual(compute_Last_Digit(10, 10), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(compute_Last_Digit(0, 0), 1)
        self.assertEqual(compute_Last_Digit(1, 0), 0)
        self.assertEqual(compute_Last_Digit(0, 1), 0)
        self.assertEqual(compute_Last_Digit(1, 2), 0)
        self.assertEqual(compute_Last_Digit(2, 1), 0)
        self.assertEqual(compute_Last_Digit(5, 10), 0)
        self.assertEqual(compute_Last_Digit(10, 5), 0)

    def test_more_complex_scenarios(self):
        self.assertEqual(compute_Last_Digit(1, 3), 3)
        self.assertEqual(compute_Last_Digit(2, 4), 4)
        self.assertEqual(compute_Last_Digit(3, 5), 5)
        self.assertEqual(compute_Last_Digit(4, 6), 6)
        self.assertEqual(compute_Last_Digit(5, 7), 7)
        self.assertEqual(compute_Last_Digit(6, 8), 8)
        self.assertEqual(compute_Last_Digit(7, 9), 9)
        self.assertEqual(compute_Last_Digit(8, 10), 0)
