import unittest
from mbpp_438_code import count_bidirectional

class TestCountBidirectional(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_bidirectional([(1, 2), (2, 3), (3, 4), (4, 5)]), '4')

    def test_empty_list(self):
        self.assertEqual(count_bidirectional([]), '0')

    def test_single_element_list(self):
        self.assertEqual(count_bidirectional([(1, 1)]), '0')

    def test_list_with_duplicates(self):
        self.assertEqual(count_bidirectional([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]), '0')

    def test_list_with_non_matching_elements(self):
        self.assertEqual(count_bidirectional([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]), '0')

    def test_list_with_non_tuple_elements(self):
        self.assertRaises(TypeError, count_bidirectional, [1, 2, 3, 4, 5])
