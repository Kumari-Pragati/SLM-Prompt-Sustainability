import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):

    def test_simple_insertion(self):
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 6), 5)

    def test_empty_list(self):
        self.assertEqual(right_insertion([], 1), 0)

    def test_insertion_at_beginning(self):
        self.assertEqual(right_insertion([2, 3, 4, 5], 1), 0)

    def test_insertion_at_end(self):
        self.assertEqual(right_insertion([1, 2, 3, 4], 5), 4)

    def test_duplicate_values(self):
        self.assertEqual(right_insertion([1, 2, 2, 3, 4], 2), 2)

    def test_negative_values(self):
        self.assertEqual(right_insertion([-5, -4, -3, -2, -1], -2), 2)

    def test_insertion_with_same_value(self):
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 3), 2)

    def test_insertion_with_large_value(self):
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 100), 5)
