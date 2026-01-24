import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_on_occurence([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_on_occurence([(1, 1)]), [(1, 1, 1)])

    def test_multiple_elements_same_occurrence(self):
        self.assertEqual(sort_on_occurence([(1, 1), (2, 2), (3, 3)]), [(1, 1, 1), (2, 2, 2), (3, 3, 1)])

    def test_multiple_elements_different_occurrence(self):
        self.assertEqual(sort_on_occurence([(1, 1), (1, 2), (2, 1), (2, 2)]), [(1, 2, 2), (2, 1, 2), (1, 1, 1), (2, 2, 1)])

    def test_negative_numbers(self):
        self.assertEqual(sort_on_occurence([(-1, 1), (0, 2), (1, 3), (-1, 2)]), [(-1, 2, 2), (0, 2, 1), (1, 3, 1), (-1, 1, 1)])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            sort_on_occurence([(1, 'a'), (2, 3), (1, 1)])

    def test_duplicate_tuples(self):
        self.assertEqual(sort_on_occurence([((1, 1),), ((1, 1),)]), [((1, 1), 2, 1)])
