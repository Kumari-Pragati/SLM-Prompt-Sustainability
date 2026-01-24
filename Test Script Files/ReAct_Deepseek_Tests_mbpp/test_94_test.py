import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 5), (2, 3), (3, 4)]
        self.assertEqual(index_minimum(test_list), 2)

    def test_edge_case_single_element(self):
        test_list = [(1, 5)]
        self.assertEqual(index_minimum(test_list), 1)

    def test_edge_case_empty_list(self):
        test_list = []
        with self.assertRaises(ValueError):
            index_minimum(test_list)

    def test_edge_case_same_minimum_values(self):
        test_list = [(1, 5), (2, 5), (3, 5)]
        self.assertIn(index_minimum(test_list), [1, 2, 3])

    def test_explicitly_handled_error_case(self):
        test_list = [(1, 'a'), (2, 'b'), (3, 'c')]
        with self.assertRaises(TypeError):
            index_minimum(test_list)
