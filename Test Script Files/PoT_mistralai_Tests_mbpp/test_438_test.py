import unittest
from mbpp_438_code import count_bidirectional

class TestCountBidirectional(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_bidirectional([(1, 2), (2, 3), (3, 4), (4, 1)]), '3')

    def test_edge_case_empty_list(self):
        self.assertEqual(count_bidirectional([]), '0')

    def test_edge_case_single_item(self):
        self.assertEqual(count_bidirectional([(1, 1)]), '0')

    def test_edge_case_two_items(self):
        self.assertEqual(count_bidirectional([(1, 2), (2, 1)]), '1')

    def test_corner_case_same_first_and_last(self):
        self.assertEqual(count_bidirectional([(1, 2), (2, 1), (1, 1)]), '1')

    def test_corner_case_repeated_values(self):
        self.assertEqual(count_bidirectional([(1, 1), (2, 2), (1, 2), (2, 1)]), '2')
