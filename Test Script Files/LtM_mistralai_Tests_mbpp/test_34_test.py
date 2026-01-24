import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 5], 5), 6)

    def test_edge_case_min(self):
        self.assertEqual(find_missing([1], 1), 2)

    def test_edge_case_max(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6], 7), 7)

    def test_missing_in_middle(self):
        self.assertEqual(find_missing([1, 2, 4, 5], 4), 3)

    def test_missing_at_beginning(self):
        self.assertEqual(find_missing([4, 5], 4), 1)

    def test_missing_at_end(self):
        self.assertEqual(find_missing([1, 2, 3], 4), -1)

    def test_duplicate_values(self):
        self.assertEqual(find_missing([1, 1, 2, 3], 4), -1)

    def test_invalid_input(self):
        self.assertRaises(ValueError, find_missing, [1, 2, 3], 0)
        self.assertRaises(ValueError, find_missing, [], 5)
        self.assertRaises(ValueError, find_missing, [1], 1)
