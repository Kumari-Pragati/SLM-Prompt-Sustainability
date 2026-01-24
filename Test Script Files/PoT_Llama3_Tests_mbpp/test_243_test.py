import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_on_occurence([[1, 2, 3], [4, 5, 6]]), 
                         [(1, 2, 3, 1), (4, 5, 6, 1)])

    def test_edge_case(self):
        self.assertEqual(sort_on_occurence([[1, 2, 3], [1, 4, 5]]), 
                         [(1, 2, 3, 1), (1, 4, 5, 1)])

    def test_edge_case2(self):
        self.assertEqual(sort_on_occurence([[1, 2, 3], [2, 4, 5]]), 
                         [(1, 2, 3, 1), (2, 4, 5, 1)])

    def test_edge_case3(self):
        self.assertEqual(sort_on_occurence([[1, 2, 3], [3, 4, 5]]), 
                         [(1, 2, 3, 1), (3, 4, 5, 1)])

    def test_empty_input(self):
        self.assertEqual(sort_on_occurence([]), [])

    def test_single_input(self):
        self.assertEqual(sort_on_occurence([[1, 2, 3]]), 
                         [(1, 2, 3, 1)])

    def test_single_input2(self):
        self.assertEqual(sort_on_occurence([[1, 1, 1]]), 
                         [(1, 1, 1, 1)])
