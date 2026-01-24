import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):
    def test_positive_list_and_valid_n(self):
        self.assertEqual(max_of_nth([(1, 2), (3, 4), (5, 6)], 1), 2)
        self.assertEqual(max_of_nth([(1, 2), (3, 4), (5, 6)], 0), 1)
        self.assertEqual(max_of_nth([(1, 2), (3, 4), (5, 6)], 2), 6)

    def test_empty_list(self):
        self.assertRaises(IndexError, max_of_nth, [], 0)

    def test_negative_list(self):
        self.assertRaises(ValueError, max_of_nth, [(-1, -2), (-3, -4), (-5, -6)], 0)

    def test_negative_n(self):
        self.assertRaises(ValueError, max_of_nth, [(1, 2), (3, 4), (5, 6)], -1)
