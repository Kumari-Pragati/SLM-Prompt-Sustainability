import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [[3, 2, 1], [6, 5, 4]]
        expected_output = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_edge_condition(self):
        list1 = [[]]
        expected_output = [[]]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_boundary_condition(self):
        list1 = [None]
        with self.assertRaises(TypeError):
            sort_sublists(list1)

    def test_invalid_input(self):
        list1 = 'not a list'
        with self.assertRaises(TypeError):
            sort_sublists(list1)
