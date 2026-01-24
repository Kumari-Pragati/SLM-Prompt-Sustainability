import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):

    def test_simple_insertion(self):
        self.assertEqual(left_insertion([1, 3, 5], 3), 1)
        self.assertEqual(left_insertion([1, 3, 5], 4), 2)
        self.assertEqual(left_insertion([1, 3, 5], 5), 2)

    def test_empty_list(self):
        self.assertEqual(left_insertion([], 3), 0)

    def test_insertion_at_beginning(self):
        self.assertEqual(left_insertion([2, 3, 4], 1), 0)

    def test_insertion_at_end(self):
        self.assertEqual(left_insertion([1, 2, 3], 4), 3)

    def test_duplicate_values(self):
        self.assertEqual(left_insertion([1, 2, 2, 3], 2), 1)

    def test_negative_values(self):
        self.assertEqual(left_insertion([-1, 0, 1], -2), 0)

    def test_insertion_with_same_value(self):
        self.assertEqual(left_insertion([1, 2, 3], 2), 1)
