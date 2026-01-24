import unittest
from mbpp_438_code import count_bidirectional

class TestCountBidirectional(unittest.TestCase):

    def test_count_bidirectional(self):
        self.assertEqual(count_bidirectional([['a', 'b'], ['b', 'c'], ['c', 'a']]), '2')
        self.assertEqual(count_bidirectional([['a', 'b'], ['b', 'c'], ['c', 'd']]), '0')
        self.assertEqual(count_bidirectional([['a', 'a'], ['b', 'b'], ['c', 'c']]), '3')
        self.assertEqual(count_bidirectional([['a', 'b'], ['b', 'a']]), '1')
        self.assertEqual(count_bidirectional([['a', 'a'], ['b', 'b'], ['c', 'c'], ['d', 'd']]), '4')
        self.assertEqual(count_bidirectional([]), '0')
        self.assertEqual(count_bidirectional([['a', 'a']]), '1')
