import unittest
from mbpp_438_code import count_bidirectional

class TestCountBidirectional(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('a', 'b'), ('b', 'c'), ('c', 'a')]
        self.assertEqual(count_bidirectional(test_list), '1')

    def test_empty_list(self):
        test_list = []
        self.assertEqual(count_bidirectional(test_list), '0')

    def test_no_matching_pairs(self):
        test_list = [('a', 'b'), ('b', 'c'), ('c', 'd')]
        self.assertEqual(count_bidirectional(test_list), '0')

    def test_all_matching_pairs(self):
        test_list = [('a', 'b'), ('b', 'a'), ('c', 'd'), ('d', 'c')]
        self.assertEqual(count_bidirectional(test_list), '2')

    def test_single_element(self):
        test_list = [('a', 'b')]
        self.assertEqual(count_bidirectional(test_list), '0')

    def test_duplicate_elements(self):
        test_list = [('a', 'a'), ('b', 'b'), ('c', 'c')]
        self.assertEqual(count_bidirectional(test_list), '0')

    def test_large_input(self):
        test_list = [(str(i), str(i+1)) for i in range(1000)]
        self.assertEqual(count_bidirectional(test_list), '495')
