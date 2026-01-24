import unittest
from mbpp_438_code import count_bidirectional

class TestCountBidirectional(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [('a', 'b'), ('b', 'c'), ('c', 'a')]
        self.assertEqual(count_bidirectional(test_list), '1')

    def test_edge_condition(self):
        test_list = []
        self.assertEqual(count_bidirectional(test_list), '0')

    def test_boundary_condition(self):
        test_list = [('a', 'b')]
        self.assertEqual(count_bidirectional(test_list), '0')

    def test_invalid_input(self):
        test_list = [('a', 'b'), ('b', 'c'), ('c', 'd')]
        with self.assertRaises(TypeError):
            count_bidirectional(test_list)
