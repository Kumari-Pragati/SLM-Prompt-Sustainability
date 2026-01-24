import unittest
from mbpp_438_code import count_bidirectional

class TestCountBidirectional(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_bidirectional([('a', 'b'), ('b', 'c'), ('c', 'a')]), '1')

    def test_empty_list(self):
        self.assertEqual(count_bidirectional([]), '0')

    def test_single_element(self):
        self.assertEqual(count_bidirectional([('a', 'b')]), '0')

    def test_no_matching_pairs(self):
        self.assertEqual(count_bidirectional([('a', 'c'), ('b', 'd')]), '0')

    def test_multiple_matching_pairs(self):
        self.assertEqual(count_bidirectional([('a', 'b'), ('b', 'a'), ('c', 'd'), ('d', 'c')]), '2')

    def test_duplicate_pairs(self):
        self.assertEqual(count_bidirectional([('a', 'b'), ('b', 'a'), ('a', 'b')]), '1')
