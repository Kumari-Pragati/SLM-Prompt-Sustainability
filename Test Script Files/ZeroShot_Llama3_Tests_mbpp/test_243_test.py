import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):

    def test_sort_on_occurence(self):
        self.assertEqual(sort_on_occurence([('a', 'b', 'c'), ('a', 'd', 'e'), ('f', 'g', 'h')]), 
                         [('a', 'b', 'c', 'd', 'e', 2), ('f', 'g', 'h', 3, 1)])
        self.assertEqual(sort_on_occurence([('a', 'b', 'c'), ('a', 'd', 'e'), ('f', 'g', 'h'), ('f', 'i', 'j')]), 
                         [('a', 'b', 'c', 'd', 'e', 2), ('f', 'g', 'h', 3, 1), ('f', 'i', 'j', 3, 2)])
        self.assertEqual(sort_on_occurence([('a', 'b', 'c'), ('a', 'd', 'e'), ('f', 'g', 'h'), ('f', 'i', 'j'), ('f', 'k', 'l')]), 
                         [('a', 'b', 'c', 'd', 'e', 2), ('f', 'g', 'h', 3, 1), ('f', 'i', 'j', 3, 2), ('f', 'k', 'l', 3, 3)])

    def test_sort_on_occurence_empty_list(self):
        self.assertEqual(sort_on_occurence([]), [])

    def test_sort_on_occurence_single_element(self):
        self.assertEqual(sort_on_occurence([('a', 'b', 'c')]), [('a', 'b', 'c', 1, 1)])
