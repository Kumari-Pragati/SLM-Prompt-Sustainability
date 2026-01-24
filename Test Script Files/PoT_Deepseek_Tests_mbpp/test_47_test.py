import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(compute_Last_Digit(1, 5), 120)
        self.assertEqual(compute_Last_Digit(10, 15), 6)
        self.assertEqual(compute_Last_Digit(20, 25), 8)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(compute_Last_Digit(0, 0), 1)
        self.assertEqual(compute_Last_Digit(10, 10), 1)
        self.assertEqual(compute_Last_Digit(0, 5), 0)
        self.assertEqual(compute_Last_Digit(10, 15), 6)

    def test_invalid_or_exceptional_inputs(self):
        with self.assertRaises(TypeError):
            compute_Last_Digit("1", 2)
        with self.assertRaises(TypeError):
            compute_Last_Digit(1, "2")
        with self.assertRaises(ValueError):
            compute_Last_Digit(-1, 2)
        with self.assertRaises(ValueError):
            compute_Last_Digit(2, -1)
        with self.assertRaises(ValueError):
            compute_Last_Digit(20, 10)
