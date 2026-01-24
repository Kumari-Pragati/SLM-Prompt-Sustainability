import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(min_Operations(6, 3), 2)

    def test_edge_case_A_greater_than_B(self):
        self.assertEqual(min_Operations(9, 6), 2)

    def test_edge_case_A_equal_to_B(self):
        self.assertEqual(min_Operations(6, 6), 1)

    def test_edge_case_A_and_B_zero(self):
        with self.assertRaises(ZeroDivisionError):
            min_Operations(0, 0)

    def test_edge_case_A_zero_B_non_zero(self):
        self.assertEqual(min_Operations(0, 3), 3)

    def test_edge_case_B_zero_A_non_zero(self):
        self.assertEqual(min_Operations(3, 0), 3)

    def test_invalid_input_type_A(self):
        with self.assertRaises(TypeError):
            min_Operations('a', 3)

    def test_invalid_input_type_B(self):
        with self.assertRaises(TypeError):
            min_Operations(3, 'b')
