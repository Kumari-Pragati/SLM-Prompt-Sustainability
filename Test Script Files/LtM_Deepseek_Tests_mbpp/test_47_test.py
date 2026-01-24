import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(compute_Last_Digit(1, 1), 1)
        self.assertEqual(compute_Last_Digit(5, 5), 5)
        self.assertEqual(compute_Last_Digit(10, 10), 0)

    def test_edge_conditions(self):
        self.assertEqual(compute_Last_Digit(1, 10), 1)
        self.assertEqual(compute_Last_Digit(10, 1), 0)
        self.assertEqual(compute_Last_Digit(1, 100), 1)
        self.assertEqual(compute_Last_Digit(100, 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(compute_Last_Digit(1, 1000), 1)
        self.assertEqual(compute_Last_Digit(1000, 1), 0)
        self.assertEqual(compute_Last_Digit(1, 10000), 1)
        self.assertEqual(compute_Last_Digit(10000, 1), 0)

    def test_complex_cases(self):
        self.assertEqual(compute_Last_Digit(15, 20), 0)
        self.assertEqual(compute_Last_Digit(20, 30), 8)
        self.assertEqual(compute_Last_Digit(30, 40), 6)
