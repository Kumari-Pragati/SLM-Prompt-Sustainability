import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):

    def test_sort_on_occurence(self):
        self.assertEqual(sort_on_occurence([('a', 1), ('b', 2), ('c', 3)]), 
                         [('a', 1, 1), ('b', 2, 1), ('c', 3, 1)])
        self.assertEqual(sort_on_occurence([('a', 1), ('a', 2), ('b', 3)]), 
                         [('a', 1, 1), ('a', 2, 1), ('b', 3, 1)])
        self.assertEqual(sort_on_occurence([('a', 1), ('b', 2), ('a', 3)]), 
                         [('a', 1, 1), ('b', 2, 1), ('a', 3, 1)])
        self.assertEqual(sort_on_occurence([('a', 1), ('b', 2), ('c', 3), ('a', 2), ('b', 3), ('c', 2)]), 
                         [('a', 1, 1), ('b', 2, 1), ('c', 3, 1), ('a', 2, 1), ('b', 3, 1), ('c', 2, 1)])
