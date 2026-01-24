import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sort_list([1, 2, 3]), '[1, 2, 3]')

    def test_edge_boundary_conditions(self):
        self.assertEqual(sort_list([0]), '[0]')
        self.assertEqual(sort_list([10]), '[10]')
        self.assertEqual(sort_list([99]), '[99]')
        self.assertEqual(sort_list([100]), '[100]')
        self.assertEqual(sort_list([-1]), '[-1]')
        self.assertEqual(sort_list([-99]), '[-99]')
        self.assertEqual(sort_list([-100]), '[-100]')

    def test_more_complex_cases(self):
        self.assertEqual(sort_list([10, 20, 30]), '[10, 20, 30]')
        self.assertEqual(sort_list([99, 999]), '[99, 999]')
        self.assertEqual(sort_list([100, 200, 300]), '[100, 200, 300]')
        self.assertEqual(sort_list([-10, -20, -30]), '[-30, -20, -10]')
        self.assertEqual(sort_list([-99, -999]), '[-999, -99]')
        self.assertEqual(sort_list([-100, -200, -300]), '[-300, -200, -100]')
        self.assertEqual(sort_list([1, 10, 100]), '[1, 10, 100]')
        self.assertEqual(sort_list([9, 99, 999]), '[9, 99, 999]')
        self.assertEqual(sort_list([10, 20, 30, 40]), '[10, 20, 30, 40]')
        self.assertEqual(sort_list([99, 999, 1000]), '[99, 999, 1000]')
