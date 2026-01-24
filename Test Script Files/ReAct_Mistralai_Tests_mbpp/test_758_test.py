import unittest
from mbpp_758_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(unique_sublists([]), {})

    def test_single_element_list(self):
        self.assertEqual(unique_sublists([[1]]), {'(1,)': 1})

    def test_single_sublist(self):
        self.assertEqual(unique_sublists([[1, 2]]), {'(1, 2)': 1})

    def test_multiple_sublists_same_order(self):
        self.assertEqual(unique_sublists([[1, 2], [1, 2]]), {'(1, 2)': 2})

    def test_multiple_sublists_different_order(self):
        self.assertEqual(unique_sublists([[2, 1], [1, 2]]), {'(1, 2)': 2})

    def test_multiple_unique_sublists(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 3], [1, 3]]), {'(1, 2)': 1, '(2, 3)': 1})

    def test_sublist_with_duplicates(self):
        self.assertEqual(unique_sublists([[1, 1, 2], [1, 2]]), {'(1, 1, 2)': 1, '(1, 2)': 1})

    def test_sublist_with_repeated_sublist(self):
        self.assertEqual(unique_sublists([[1, 2], [1, 2], [1, 2]]), {'(1, 2)': 3})

    def test_sublist_with_empty_list(self):
        self.assertEqual(unique_sublists([[1, 2], [], [3]]), {'(1, 2)': 1, '(3)': 1})

    def test_sublist_with_negative_numbers(self):
        self.assertEqual(unique_sublists([[-1, 2], [1, -1]]), {'(-1, 2)': 1, '(1, -1)': 1})

    def test_sublist_with_mixed_types(self):
        self.assertRaises(TypeError, unique_sublists, [[1, 'a'], [2, 3]])
