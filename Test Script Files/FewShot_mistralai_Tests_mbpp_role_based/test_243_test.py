import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_on_occurence([]), [])

    def test_single_item(self):
        self.assertEqual(sort_on_occurence([(1, 1)]), [(1, 1, 1, 1)])

    def test_multiple_items_same_occurrence(self):
        self.assertEqual(sort_on_occurence([(1, 1), (2, 2), (3, 3)]), [(1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3)])

    def test_multiple_items_different_occurrence(self):
        self.assertEqual(sort_on_occurence([(1, 1), (1, 2), (2, 1), (2, 2)]), [(1, 1, 2, 1), (1, 2, 2, 2), (2, 1, 1, 2), (2, 2, 1, 2)])

    def test_list_with_duplicate_tuples(self):
        self.assertEqual(sort_on_occurence([(1, 1), (1, 1)]), [(1, 1, 2, 1)])

    def test_list_with_non_tuple_elements(self):
        with self.assertRaises(TypeError):
            sort_on_occurence([1, 2, 3])
