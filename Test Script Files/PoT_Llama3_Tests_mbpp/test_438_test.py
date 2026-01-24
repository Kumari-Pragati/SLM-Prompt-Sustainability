import unittest
from mbpp_438_code import count_bidirectional

class TestCountBidirectional(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_bidirectional([]), '0')

    def test_single_element_list(self):
        self.assertEqual(count_bidirectional([['a', 'b']]), '0')

    def test_no_bidirectional_pairs(self):
        self.assertEqual(count_bidirectional([['a', 'b'], ['b', 'c'], ['c', 'd']]), '0')

    def test_one_bidirectional_pair(self):
        self.assertEqual(count_bidirectional([['a', 'b'], ['b', 'a']]), '1')

    def test_multiple_bidirectional_pairs(self):
        self.assertEqual(count_bidirectional([['a', 'b'], ['b', 'a'], ['c', 'd'], ['d', 'c']]), '2')

    def test_bidirectional_pairs_with_duplicates(self):
        self.assertEqual(count_bidirectional([['a', 'b'], ['b', 'a'], ['a', 'b']]), '1')

    def test_bidirectional_pairs_with_duplicates_and_non_bidirectional(self):
        self.assertEqual(count_bidirectional([['a', 'b'], ['b', 'a'], ['a', 'c']]), '1')
