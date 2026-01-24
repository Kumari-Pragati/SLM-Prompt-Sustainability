import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(compute_Last_Digit(1, 2), 2)
        self.assertEqual(compute_Last_Digit(10, 11), 1)
        self.assertEqual(compute_Last_Digit(100, 101), 0)

    def test_edge_case(self):
        self.assertEqual(compute_Last_Digit(0, 1), 1)
        self.assertEqual(compute_Last_Digit(1, 0), 1)
        self.assertEqual(compute_Last_Digit(1, 1), 1)
        self.assertEqual(compute_Last_Digit(100, 100), 1)

    def test_boundary_case(self):
        self.assertEqual(compute_Last_Digit(0, 4), 0)
        self.assertEqual(compute_Last_Digit(4, 5), 0)
        self.assertEqual(compute_Last_Digit(5, 99), 0)
        self.assertEqual(compute_Last_Digit(99, 100), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            compute_Last_Digit('a', 'b')
        with self.assertRaises(TypeError):
            compute_Last_Digit(1.0, 2.0)
        with self.assertRaises(TypeError):
            compute_Last_Digit([1, 2], [3, 4])
