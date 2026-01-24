import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(compute_Last_Digit(1, 5), 120)

    def test_boundary_case(self):
        self.assertEqual(compute_Last_Digit(10, 10), 1)

    def test_edge_case(self):
        self.assertEqual(compute_Last_Digit(1, 1), 1)
        self.assertEqual(compute_Last_Digit(1, 6), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            compute_Last_Digit('a', 5)
        with self.assertRaises(TypeError):
            compute_Last_Digit(5, 'b')
