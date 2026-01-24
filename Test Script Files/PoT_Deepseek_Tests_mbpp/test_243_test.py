import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_on_occurence([('a', 1), ('b', 2), ('a', 3)]), [('a', 1, 3), ('b', 2, 1)])

    def test_edge_case_single_element(self):
        self.assertEqual(sort_on_occurence([('a', 1)]), [('a', 1, 1)])

    def test_boundary_case_empty_list(self):
        self.assertEqual(sort_on_occurence([]), [])

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(sort_on_occurence([('a', 1), ('a', 1)]), [('a', 1, 2)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_on_occurence([('a', 1), 'b'])
