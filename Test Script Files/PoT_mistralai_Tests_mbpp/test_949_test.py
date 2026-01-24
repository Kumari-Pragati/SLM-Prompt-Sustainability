import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):

    def test_sort_list_typical(self):
        self.assertEqual(sort_list([1, 10, 2, 3, 4]), "[1, 2, 3, 4, 10]")
        self.assertEqual(sort_list([100, 10, 2, 3, 400]), "[2, 3, 10, 100, 400]")
        self.assertEqual(sort_list([1.1, 10.01, 2, 3, 4]), "[2, 3, 4, 1.1, 10.01]")

    def test_sort_list_edge_cases(self):
        self.assertEqual(sort_list([0, 0, 0]), "[0, 0, 0]")
        self.assertEqual(sort_list([9, 9, 9]), "[9, 9, 9]")
        self.assertEqual(sort_list([-1, -10, -2, -3, -4]), "[-4, -3, -2, -10, -1]")

    def test_sort_list_corner_cases(self):
        self.assertEqual(sort_list([1, 10, 2, 3, 4, 10, 1]), "[1, 1, 2, 3, 4, 10, 10]")
        self.assertEqual(sort_list([1, 10, 2, 3, 4, 0]), "[0, 1, 2, 3, 4, 10]")
        self.assertEqual(sort_list([1, 10, 2, 3, 4, "10"]), "[1, 1, 2, 3, 4, "10"]")
        self.assertEqual(sort_list([1, 10, 2, 3, 4, None]), "[None, 1, 2, 3, 4, 10]")
