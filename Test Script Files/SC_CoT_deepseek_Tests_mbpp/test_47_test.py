import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(compute_Last_Digit(5, 10), 1)

    def test_edge_case(self):
        self.assertEqual(compute_Last_Digit(10, 10), 1)
        self.assertEqual(compute_Last_Digit(15, 20), 0)

    def test_boundary_case(self):
        self.assertEqual(compute_Last_Digit(0, 1), 1)
        self.assertEqual(compute_Last_Digit(10, 15), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            compute_Last_Digit("5", 10)
        with self.assertRaises(TypeError):
            compute_Last_Digit(5, "10")
        with self.assertRaises(TypeError):
            compute_Last_Digit("5", "10")
