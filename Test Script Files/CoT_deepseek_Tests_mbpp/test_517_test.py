import unittest
from mbpp_517_code import largest_pos

class TestLargestPos(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(largest_pos([1, 2, 3, 4, 5]), 5)

    def test_single_element(self):
        self.assertEqual(largest_pos([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(largest_pos([-1, -2, -3, -4, -5]), -1)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            largest_pos([])

    def test_large_numbers(self):
        self.assertEqual(largest_pos([1000000, 2000000, 3000000]), 3000000)

    def test_duplicate_largest(self):
        self.assertEqual(largest_pos([5, 5, 5, 4, 3, 2, 1]), 5)
