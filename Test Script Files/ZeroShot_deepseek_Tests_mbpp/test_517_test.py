import unittest
from mbpp_517_code import largest_pos

class TestLargestPos(unittest.TestCase):

    def test_largest_pos_positive_numbers(self):
        self.assertEqual(largest_pos([1, 2, 3, 4, 5]), 5)

    def test_largest_pos_negative_numbers(self):
        self.assertEqual(largest_pos([-1, -2, -3, -4, -5]), -1)

    def test_largest_pos_mixed_numbers(self):
        self.assertEqual(largest_pos([-1, 2, -3, 4, -5]), 4)

    def test_largest_pos_empty_list(self):
        self.assertIsNone(largest_pos([]))

    def test_largest_pos_single_element(self):
        self.assertEqual(largest_pos([1]), 1)
