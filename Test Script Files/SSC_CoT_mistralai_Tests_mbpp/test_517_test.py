import unittest
from mbpp_517_code import largest_pos

class TestLargestPos(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(largest_pos([1, 2, 3, 4, 5]), 5)
        self.assertEqual(largest_pos([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(largest_pos([0, 0, 0, 0, 0]), 0)

    def test_edge_cases(self):
        self.assertEqual(largest_pos([1]), 1)
        self.assertEqual(largest_pos([-1]), -1)
        self.assertEqual(largest_pos([1, -1]), 1)
        self.assertEqual(largest_pos([-1, 1]), -1)
        self.assertEqual(largest_pos([-1, -1]), -1)
        self.assertEqual(largest_pos([1, 1]), 1)

    def test_empty_list(self):
        self.assertIsNone(largest_pos([]))

    def test_float_input(self):
        self.assertEqual(largest_pos([1.0, 2.0, 3.0]), 3.0)
        self.assertEqual(largest_pos([-1.0, -2.0, -3.0]), -1.0)

    def test_mixed_input(self):
        self.assertEqual(largest_pos([1, 2.0, 3]), 3)
        self.assertEqual(largest_pos([-1, -2.0, -3]), -1)
