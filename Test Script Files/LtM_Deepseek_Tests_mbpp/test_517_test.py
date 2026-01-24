import unittest
from mbpp_517_code import largest_pos

class TestLargestPos(unittest.TestCase):

    def test_simple_positive_numbers(self):
        self.assertEqual(largest_pos([1, 2, 3, 4, 5]), 5)
        self.assertEqual(largest_pos([10, 20, 30, 40, 50]), 50)

    def test_negative_numbers(self):
        self.assertEqual(largest_pos([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(largest_pos([-10, -20, -30, -40, -50]), -10)

    def test_mixed_numbers(self):
        self.assertEqual(largest_pos([-1, 2, -3, 4, -5]), 4)
        self.assertEqual(largest_pos([-10, 20, -30, 40, -50]), 40)

    def test_empty_list(self):
        self.assertIsNone(largest_pos([]))

    def test_single_element_list(self):
        self.assertEqual(largest_pos([1]), 1)
        self.assertEqual(largest_pos([-1]), -1)

    def test_maximum_value(self):
        self.assertEqual(largest_pos([float('inf')]), float('inf'))

    def test_minimum_value(self):
        self.assertEqual(largest_pos([float('-inf')]), float('-inf'))
