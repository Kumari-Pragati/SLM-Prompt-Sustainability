import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(right_insertion([1, 3, 5, 7], 5), 2)

    def test_already_exists(self):
        self.assertEqual(right_insertion([1, 3, 5, 7], 5), 2)

    def test_insert_at_beginning(self):
        self.assertEqual(right_insertion([3, 5, 7], 1), 0)

    def test_insert_at_end(self):
        self.assertEqual(right_insertion([1, 3, 5], 7), 3)

    def test_empty_list(self):
        self.assertEqual(right_insertion([], 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(right_insertion([-7, -5, -3, -1], -5), 1)

    def test_duplicate_numbers(self):
        self.assertEqual(right_insertion([1, 1, 3, 5, 7], 1), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            right_insertion("not a list", 5)
