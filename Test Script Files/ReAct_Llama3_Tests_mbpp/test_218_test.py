import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_Operations(10, 5), 4)

    def test_edge_case_A_greater_than_B(self):
        self.assertEqual(min_Operations(5, 10), 4)

    def test_edge_case_A_equal_to_B(self):
        self.assertEqual(min_Operations(5, 5), 4)

    def test_edge_case_A_and_B_zero(self):
        with self.assertRaises(ZeroDivisionError):
            min_Operations(0, 0)

    def test_edge_case_A_zero_B_nonzero(self):
        self.assertEqual(min_Operations(0, 5), 5)

    def test_edge_case_B_zero_A_nonzero(self):
        self.assertEqual(min_Operations(5, 0), 5)

    def test_edge_case_A_and_B_negative(self):
        self.assertEqual(min_Operations(-5, -10), 4)

    def test_edge_case_A_negative_B_nonnegative(self):
        self.assertEqual(min_Operations(-5, 10), 4)

    def test_edge_case_B_negative_A_nonnegative(self):
        self.assertEqual(min_Operations(5, -10), 4)
