import unittest
from mbpp_438_code import count_bidirectional

class TestCountBidirectional(unittest.TestCase):
    def test_typical_input(self):
        test_list = [('a', 'b'), ('b', 'c'), ('c', 'd')]
        self.assertEqual(count_bidirectional(test_list), '2')

    def test_edge_case_empty_list(self):
        test_list = []
        self.assertEqual(count_bidirectional(test_list), '0')

    def test_edge_case_single_element_list(self):
        test_list = [('a', 'a')]
        self.assertEqual(count_bidirectional(test_list), '0')

    def test_edge_case_two_element_list(self):
        test_list = [('a', 'b')]
        self.assertEqual(count_bidirectional(test_list), '0')

    def test_edge_case_duplicates(self):
        test_list = [('a', 'a'), ('a', 'b'), ('b', 'a')]
        self.assertEqual(count_bidirectional(test_list), '1')

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            count_bidirectional('invalid_input')

    def test_invalid_input_non_list_of_tuples(self):
        with self.assertRaises(TypeError):
            count_bidirectional([1, 2, 3])

    def test_invalid_input_non_list_of_tuples_of_integers(self):
        with self.assertRaises(TypeError):
            count_bidirectional([(1, 2), (3, 4)])

    def test_edge_case_duplicates_in_order(self):
        test_list = [('a', 'a'), ('a', 'b'), ('b', 'a')]
        self.assertEqual(count_bidirectional(test_list), '1')

    def test_edge_case_duplicates_out_of_order(self):
        test_list = [('a', 'b'), ('b', 'a'), ('a', 'a')]
        self.assertEqual(count_bidirectional(test_list), '1')
