import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sort_on_occurence([(1, 2), (1, 3), (2, 2), (2, 3), (3, 1), (3, 2)]), [((1, 2), 2, 2), ((1, 3), 2, 2), ((2, 2), 2, 1), ((2, 3), 2, 1), ((3, 1), 1, 1), ((3, 2), 2, 1)])

    def test_edge_input(self):
        self.assertEqual(sort_on_occurence([(1, 2)]), [((1, 2), 1, 1)])
        self.assertEqual(sort_on_occurence([(1, 2), (1, 2)]), [((1, 2), 2, 1)])

    def test_boundary_input(self):
        self.assertEqual(sort_on_occurence([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]), [((0, 0), 1, 1), ((1, 1), 2, 1), ((2, 2), 2, 1), ((3, 3), 1, 1), ((4, 4), 1, 1), ((5, 5), 1, 1)])
        self.assertEqual(sort_on_occurence([(100, 100)]), [((100, 100), 1, 1)])

    def test_complex_input(self):
        self.assertEqual(sort_on_occurence([(1, 2), (1, 3), (2, 2), (2, 3), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)]), [((1, 2), 2, 2), ((1, 3), 2, 2), ((2, 2), 2, 1), ((2, 3), 2, 1), ((3, 1), 1, 1), ((3, 2), 2, 1), ((3, 4), 1, 1), ((4, 1), 3, 1), ((4, 2), 3, 1), ((4, 3), 3, 1), ((4, 4), 1, 1)])
