import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sort_list([10, 2, 30, 4, 50]), '[2, 4, 10, 30, 50]')

    def test_edge_condition(self):
        self.assertEqual(sort_list([1]), '[1]')

    def test_boundary_condition(self):
        self.assertEqual(sort_list([100, 200, 300, 400, 500]), '[100, 200, 300, 400, 500]')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_list('10, 2, 30, 4, 50')

        with self.assertRaises(TypeError):
            sort_list(10)

        with self.assertRaises(TypeError):
            sort_list(None)
