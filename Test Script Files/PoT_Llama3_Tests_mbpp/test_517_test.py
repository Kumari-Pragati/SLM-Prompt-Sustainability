import unittest
from mbpp_517_code import largest_pos

class TestLargestPos(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(largest_pos([1, 2, 3, 4, 5]), 5)

    def test_edge_case_empty_list(self):
        self.assertIsNone(largest_pos([]))

    def test_edge_case_single_element_list(self):
        self.assertEqual(largest_pos([1]), 1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(largest_pos([-1, -2, -3, -4, -5]), -1)

    def test_edge_case_positive_numbers(self):
        self.assertEqual(largest_pos([1, 2, 3, 4, 5]), 5)

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(largest_pos([-1, 0, 1, 2, 3]), 3)

    def test_edge_case_duplicates(self):
        self.assertEqual(largest_pos([1, 2, 2, 3, 4]), 4)
