import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(left_insertion([], 5), 0)

    def test_insertion_at_start(self):
        self.assertEqual(left_insertion([1, 2, 3], 0), 0)

    def test_insertion_at_end(self):
        self.assertEqual(left_insertion([1, 2, 3], 4), 3)

    def test_insertion_in_middle(self):
        self.assertEqual(left_insertion([1, 2, 3], 2), 1)

    def test_insertion_greater_than_all(self):
        self.assertEqual(left_insertion([1, 2, 3], 4), 3)

    def test_insertion_smaller_than_all(self):
        self.assertEqual(left_insertion([1, 2, 3], 0), 0)

    def test_insertion_equal_to_all(self):
        self.assertEqual(left_insertion([1, 2, 2], 2), 1)
