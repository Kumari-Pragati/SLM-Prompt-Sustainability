import unittest
from mbpp_438_code import count_bidirectional

class TestCountBidirectional(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_bidirectional([]), '0')

    def test_single_element(self):
        self.assertEqual(count_bidirectional([(1, 1)]), '0')
        self.assertEqual(count_bidirectional([(1, 2)]), '0')

    def test_pair_elements(self):
        self.assertEqual(count_bidirectional([(1, 1), (2, 2)]), '0')
        self.assertEqual(count_bidirectional([(1, 1), (2, 1)]), '1')
        self.assertEqual(count_bidirectional([(1, 1), (1, 2)]), '0')

    def test_multiple_pairs(self):
        self.assertEqual(count_bidirectional([(1, 1), (2, 2), (1, 3)]), '1')
        self.assertEqual(count_bidirectional([(1, 1), (2, 2), (1, 1)]), '1')

    def test_duplicate_pairs(self):
        self.assertEqual(count_bidirectional([(1, 1), (1, 1)]), '1')

    def test_mixed_data_types(self):
        self.assertRaises(TypeError, count_bidirectional, [(1, 'a'), (2, 2)])

    def test_list_with_tuples_and_pairs(self):
        self.assertRaises(TypeError, count_bidirectional, [(1, 'a'), (2, 2), (1, 1)])
