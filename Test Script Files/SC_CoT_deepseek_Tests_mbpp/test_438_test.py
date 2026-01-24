import unittest

from mbpp_438_code import count_bidirectional

class TestCountBidirectional(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('a', 'b'), ('b', 'c'), ('c', 'a')]
        self.assertEqual(count_bidirectional(test_list), '1')

    def test_empty_list(self):
        test_list = []
        self.assertEqual(count_bidirectional(test_list), '0')

    def test_single_element(self):
        test_list = [('a', 'b')]
        self.assertEqual(count_bidirectional(test_list), '0')

    def test_no_matching_pairs(self):
        test_list = [('a', 'c'), ('b', 'd'), ('c', 'e')]
        self.assertEqual(count_bidirectional(test_list), '0')

    def test_multiple_matching_pairs(self):
        test_list = [('a', 'b'), ('b', 'a'), ('c', 'd'), ('d', 'c'), ('e', 'f'), ('f', 'e')]
        self.assertEqual(count_bidirectional(test_list), '2')

    def test_invalid_input(self):
        test_list = [('a', 'b'), ('b', 1), ('c', 'a')]
        with self.assertRaises(TypeError):
            count_bidirectional(test_list)
