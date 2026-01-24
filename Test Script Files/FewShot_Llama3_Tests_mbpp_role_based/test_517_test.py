import unittest
from mbpp_517_code import largest_pos

class TestLargestPos(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(largest_pos([1, 2, 3, 4, 5]), 5)

    def test_edge_case_empty_list(self):
        self.assertRaises(IndexError, largest_pos, [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(largest_pos([5]), 5)

    def test_edge_case_all_negative_numbers(self):
        self.assertEqual(largest_pos([-1, -2, -3, -4, -5]), -1)

    def test_edge_case_all_positive_numbers(self):
        self.assertEqual(largest_pos([1, 2, 3, 4, 5]), 5)

    def test_edge_case_mixed_positive_and_negative_numbers(self):
        self.assertEqual(largest_pos([-1, 2, -3, 4, -5]), 4)

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(largest_pos([1, 2, 2, 3, 4]), 4)
