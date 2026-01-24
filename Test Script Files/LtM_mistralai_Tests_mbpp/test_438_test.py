import unittest
from mbpp_438_code import count_bidirectional

class TestCountBidirectional(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_bidirectional([(1, 1), (2, 2), (3, 3)]), '2')
        self.assertEqual(count_bidirectional([(1, 2), (2, 3), (3, 1)]), '1')
        self.assertEqual(count_bidirectional([(1, 1), (1, 2), (2, 1), (2, 2)]), '1')

    def test_edge_cases(self):
        self.assertEqual(count_bidirectional([(1, 1)]), '0')
        self.assertEqual(count_bidirectional([(1, 1), (1, 1)]), '1')
        self.assertEqual(count_bidirectional([(1, 1), (1, 2), (2, 1), (2, 2), (1, 1)]), '2')
        self.assertEqual(count_bidirectional([(1, 1), (1, 2), (2, 1), (2, 2), (1, 2)]), '1')
        self.assertEqual(count_bidirectional([(1, 1), (1, 2), (2, 1), (2, 2), (2, 1)]), '1')

    def test_complex(self):
        self.assertEqual(count_bidirectional([(1, 1), (2, 2), (3, 1), (1, 2), (2, 3)]), '1')
        self.assertEqual(count_bidirectional([(1, 1), (2, 2), (3, 1), (1, 2), (2, 1)]), '1')
        self.assertEqual(count_bidirectional([(1, 1), (2, 2), (3, 1), (1, 2), (2, 3), (3, 2)]), '2')
