import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_on_occurence([]), [])

    def test_single_element(self):
        self.assertEqual(sort_on_occurence([(1, 1)]), [(1, 1, 1, 1)])

    def test_multiple_elements_same_occurrence(self):
        self.assertEqual(sort_on_occurence([(1, 1), (2, 2), (3, 3)]), [(1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3)])

    def test_multiple_elements_different_occurrence(self):
        self.assertEqual(sort_on_occurence([(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)]), [(1, 1, 2, 2, 1), (2, 1, 2, 2, 1), (3, 3, 3, 3, 1)])

    def test_mixed_data_types(self):
        self.assertEqual(sort_on_occurence([(1, 1), (2, 'a'), (3, 3.0)]), [(1, 1, 1, 1), (2, 'a', 1, 1), (3, 3.0, 1, 1)])

    def test_duplicate_tuples(self):
        self.assertEqual(sort_on_occurence([(1, 1), (1, 1), (2, 2)]), [(1, 1, 2, 2, 2)])

    def test_invalid_input(self):
        self.assertRaises(TypeError, sort_on_occurence, [(1, 'invalid'), (2, [3])])
