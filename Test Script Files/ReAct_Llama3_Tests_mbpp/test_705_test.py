import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_sublists([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(sort_sublists([3, 2, 1]), [1, 2, 3])

    def test_sublists_of_differing_lengths(self):
        self.assertEqual(sort_sublists(['hello', 'world', 'abc']), ['abc', 'hello', 'world'])

    def test_sublists_of_equal_lengths(self):
        self.assertEqual(sort_sublists(['abc', 'def', 'ghi']), ['abc', 'def', 'ghi'])

    def test_sublists_with_duplicates(self):
        self.assertEqual(sort_sublists([1, 2, 2, 3, 1]), [1, 1, 2, 2, 3])

    def test_sublists_with_negative_numbers(self):
        self.assertEqual(sort_sublists([-3, -2, -1]), [-3, -2, -1])

    def test_sublists_with_mixed_types(self):
        self.assertEqual(sort_sublists([1, 'hello', 2, 'world']), ['hello', 'world', 1, 2])
