import unittest
from mbpp_438_code import count_bidirectional

class TestCountBidirectional(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(count_bidirectional([(1, 2), (2, 3), (3, 4), (4, 1)]), '3')
        self.assertEqual(count_bidirectional([(1, 1), (2, 2), (3, 3), (4, 4)]), '0')
        self.assertEqual(count_bidirectional([(1, 2), (2, 1), (1, 3), (3, 1)]), '1')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_bidirectional([(1, 2), (2, 3), (3, 4), (4, 1), (1, 1)]), '2')
        self.assertEqual(count_bidirectional([(1, 2), (2, 3), (3, 4), (4, 1), (1, 1), (5, 5)]), '3')
        self.assertEqual(count_bidirectional([(1, 2), (2, 3), (3, 4), (4, 1), (1, 1), (5, 5), (5, 5)]), '3')
        self.assertEqual(count_bidirectional([(1, 2), (2, 3), (3, 4), (4, 1), (1, 1), (5, 5), (5, 5), (5, 5)]), '3')
        self.assertEqual(count_bidirectional([(1, 2), (2, 3), (3, 4), (4, 1), (1, 1), (5, 5), (5, 5), (5, 5), (5, 5)]), '3')

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_bidirectional, [1, 2])
        self.assertRaises(TypeError, count_bidirectional, [(1, 'a'), (2, 'b')])
