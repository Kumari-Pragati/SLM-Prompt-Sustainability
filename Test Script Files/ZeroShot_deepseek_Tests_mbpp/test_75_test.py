import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):

    def test_find_tuples_with_empty_list(self):
        self.assertEqual(find_tuples([], 2), "[]")

    def test_find_tuples_with_all_divisible_elements(self):
        self.assertEqual(find_tuples([(2, 4, 6), (8, 10, 12)], 2), "[(2, 4, 6), (8, 10, 12)]")

    def test_find_tuples_with_some_divisible_elements(self):
        self.assertEqual(find_tuples([(2, 4, 7), (8, 10, 12)], 2), "[(2, 4, 7), (8, 10, 12)]")

    def test_find_tuples_with_no_divisible_elements(self):
        self.assertEqual(find_tuples([(2, 5, 7), (8, 11, 13)], 2), "[]")
