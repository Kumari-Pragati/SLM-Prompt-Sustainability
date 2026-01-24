import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):
    def test_typical_use_case(self):
        nums = array('d', [1.0, -2.0, 3.0, -4.0, 5.0])
        self.assertEqual(positive_count(nums), 0.6)

    def test_edge_case_with_all_positive_numbers(self):
        nums = array('d', [1.0, 2.0, 3.0])
        self.assertEqual(positive_count(nums), 1.0)

    def test_edge_case_with_all_negative_numbers(self):
        nums = array('d', [-1.0, -2.0, -3.0])
        self.assertEqual(positive_count(nums), 0.0)

    def test_boundary_case_with_empty_array(self):
        nums = array('d', [])
        self.assertEqual(positive_count(nums), 0.0)

    def test_boundary_case_with_single_positive_number(self):
        nums = array('d', [1.0])
        self.assertEqual(positive_count(nums), 1.0)

    def test_boundary_case_with_single_negative_number(self):
        nums = array('d', [-1.0])
        self.assertEqual(positive_count(nums), 0.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            positive_count("not an array")
