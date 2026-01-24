import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4]), [1, 1])

    def test_edge_case_single_number(self):
        self.assertEqual(diff_consecutivenums([1]), [])

    def test_boundary_case_empty_list(self):
        self.assertEqual(diff_consecutivenums([]), [])

    def test_error_handling_non_list_input(self):
        with self.assertRaises(TypeError):
            diff_consecutivenums("1, 2, 3, 4")

    def test_error_handling_non_integer_elements(self):
        with self.assertRaises(TypeError):
            diff_consecutivenums([1, "2", 3, 4])
