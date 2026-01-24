import unittest
from mbpp_438_code import count_bidirectional

class TestCountBidirectional(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_bidirectional([]), '0')

    def test_single_element(self):
        self.assertEqual(count_bidirectional([('a', 'b')]), '0')

    def test_two_elements(self):
        self.assertEqual(count_bidirectional([('a', 'b'), ('b', 'a')]), '1')

    def test_no_bidirectional_pairs(self):
        self.assertEqual(count_bidirectional([('a', 'b'), ('b', 'c')]), '0')

    def test_multiple_bidirectional_pairs(self):
        self.assertEqual(count_bidirectional([('a', 'b'), ('b', 'a'), ('c', 'd'), ('d', 'c')]), '2')

    def test_duplicate_elements(self):
        self.assertEqual(count_bidirectional([('a', 'a'), ('b', 'b')]), '0')
