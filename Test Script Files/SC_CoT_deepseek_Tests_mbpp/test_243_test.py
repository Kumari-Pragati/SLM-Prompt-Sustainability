import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sort_on_occurence([('a', 1), ('b', 2), ('a', 3)]), 
                         [('a', 1, 3), ('b', 2, 1)])

    def test_empty_list(self):
        self.assertEqual(sort_on_occurence([]), [])

    def test_single_element(self):
        self.assertEqual(sort_on_occurence([('a', 1)]), [('a', 1, 1)])

    def test_same_occurrence(self):
        self.assertEqual(sort_on_occurence([('a', 1), ('b', 1)]), 
                         [('a', 1, 1), ('b', 1, 1)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_on_occurence([('a', 'b')])
