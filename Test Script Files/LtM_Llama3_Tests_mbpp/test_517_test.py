import unittest
from mbpp_517_code import largest_pos

class TestLargestPos(unittest.TestCase):
    def test_simple_positive(self):
        self.assertEqual(largest_pos([1, 2, 3, 4, 5]), 5)

    def test_simple_negative(self):
        self.assertEqual(largest_pos([-1, -2, -3, -4, -5]), -1)

    def test_empty_list(self):
        self.assertIsNone(largest_pos([]))

    def test_single_element(self):
        self.assertEqual(largest_pos([5]), 5)

    def test_all_negative(self):
        self.assertEqual(largest_pos([-5, -4, -3, -2, -1]), -1)

    def test_mixed_positive_negative(self):
        self.assertEqual(largest_pos([-5, -4, 3, 2, 1]), 3)

    def test_duplicates(self):
        self.assertEqual(largest_pos([1, 2, 2, 3, 4]), 4)
