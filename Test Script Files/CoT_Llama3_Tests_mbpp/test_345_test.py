import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4, 5]), [1, 1, 1])

    def test_edge_case_empty_list(self):
        self.assertEqual(diff_consecutivenums([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(diff_consecutivenums([1]), [])

    def test_edge_case_two_element_list(self):
        self.assertEqual(diff_consecutivenums([1, 1]), [])

    def test_edge_case_three_element_list(self):
        self.assertEqual(diff_consecutivenums([1, 1, 1]), [])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            diff_consecutivenums("abc")

    def test_invalid_input_non_integer_list(self):
        with self.assertRaises(TypeError):
            diff_consecutivenums([1, "a", 3])

    def test_invalid_input_non_consecutive_integer_list(self):
        with self.assertRaises(TypeError):
            diff_consecutivenums([1, 3, 5])
