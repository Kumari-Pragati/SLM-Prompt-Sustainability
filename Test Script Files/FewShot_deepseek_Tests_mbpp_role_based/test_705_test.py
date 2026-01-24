import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [['b', 'a'], ['dd', 'cc', 'bb', 'aa'], ['eee', 'ddd', 'ccc']]
        expected_output = [['aa', 'bb', 'cc', 'dd', 'ee'], ['a', 'b'], ['eee', 'ddd', 'ccc']]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_edge_condition(self):
        list1 = [[]]
        expected_output = [[]]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_boundary_condition(self):
        list1 = [['a'], ['aa'], ['aaa']]
        expected_output = [['a'], ['aa'], ['aaa']]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_sublists('not a list')
