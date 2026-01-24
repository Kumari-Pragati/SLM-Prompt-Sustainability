import unittest
from mbpp_517_code import largest_pos

class TestLargestPos(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(largest_pos([1, 2, 3, 4, 5]), 5)
        self.assertEqual(largest_pos([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(largest_pos([0, 0, 0, 0, 0]), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(largest_pos([]), None)

    def test_edge_case_single_element(self):
        self.assertEqual(largest_pos([1]), 1)
        self.assertEqual(largest_pos([-1]), -1)
        self.assertEqual(largest_pos([0]), 0)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(largest_pos([-5, -3, -1, 1, 3]), 3)
        self.assertEqual(largest_pos([-5, -3, -1, -2, 1]), -1)
        self.assertEqual(largest_pos([-5, -3, -1, -2, -4]), -4)
