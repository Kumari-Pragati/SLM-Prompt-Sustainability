import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(right_insertion([1, 3, 5, 7], 5), 2)

    def test_empty_list(self):
        self.assertEqual(right_insertion([], 5), 0)

    def test_list_with_same_elements(self):
        self.assertEqual(right_insertion([5, 5, 5], 5), 3)

    def test_insert_at_beginning(self):
        self.assertEqual(right_insertion([2, 3, 4], 1), 0)

    def test_insert_at_end(self):
        self.assertEqual(right_insertion([1, 2, 3], 4), 3)

    def test_insert_duplicate(self):
        self.assertEqual(right_insertion([1, 2, 3, 4], 3), 2)

    def test_insert_negative_number(self):
        self.assertEqual(right_insertion([1, 2, 3, 4], -1), 0)

    def test_insert_large_number(self):
        self.assertEqual(right_insertion([1, 2, 3, 4], 10), 4)
