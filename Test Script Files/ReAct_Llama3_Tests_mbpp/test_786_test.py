import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(right_insertion([], 5), 0)

    def test_insertion_at_start(self):
        self.assertEqual(right_insertion([1, 2, 3], 0), 0)

    def test_insertion_at_end(self):
        self.assertEqual(right_insertion([1, 2, 3], 4), 3)

    def test_insertion_in_middle(self):
        self.assertEqual(right_insertion([1, 2, 3], 2), 1)

    def test_insertion_greater_than_all(self):
        self.assertEqual(right_insertion([1, 2, 3], 4), 3)

    def test_insertion_smaller_than_all(self):
        self.assertEqual(right_insertion([1, 2, 3], 0), 0)

    def test_insertion_equal_to_all(self):
        self.assertEqual(right_insertion([1, 2, 3], 1), 0)
