import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(compute_Last_Digit(1, 2), 1)
        self.assertEqual(compute_Last_Digit(10, 11), 1)
        self.assertEqual(compute_Last_Digit(99, 100), 0)
        self.assertEqual(compute_Last_Digit(1000, 1001), 0)

    def test_edge_cases(self):
        self.assertEqual(compute_Last_Digit(0, 1), 1)
        self.assertEqual(compute_Last_Digit(1, 0), 1)
        self.assertEqual(compute_Last_Digit(-1, 0), 1)
        self.assertEqual(compute_Last_Digit(0, -1), 1)

    def test_boundary_cases(self):
        self.assertEqual(compute_Last_Digit(0, 0), 1)
        self.assertEqual(compute_Last_Digit(1, 1), 1)
        self.assertEqual(compute_Last_Digit(10, 10), 1)
        self.assertEqual(compute_Last_Digit(99, 99), 1)
