import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [(1, 2), (2, 1), (3, 3)]
        self.assertEqual(index_minimum(test_list), 2)

    def test_edge_condition(self):
        test_list = [(1, -1), (2, -2), (3, -3)]
        self.assertEqual(index_minimum(test_list), 1)

    def test_boundary_condition(self):
        test_list = [(1, 0), (2, 0), (3, 0)]
        self.assertEqual(index_minimum(test_list), 1)

    def test_invalid_input(self):
        test_list = [(1, 'a'), (2, 'b'), (3, 'c')]
        with self.assertRaises(TypeError):
            index_minimum(test_list)
