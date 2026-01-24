import unittest
from mbpp_438_code import count_bidirectional

class TestCountBidirectional(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_bidirectional([]), '0')

    def test_single_element(self):
        self.assertEqual(count_bidirectional([(1, 1)]), '0')

    def test_pair_of_elements(self):
        self.assertEqual(count_bidirectional([(1, 2), (2, 1)]), '1')

    def test_multiple_pairs(self):
        self.assertEqual(count_bidirectional([(1, 2), (2, 3), (3, 1)]), '1')

    def test_duplicate_pairs(self):
        self.assertEqual(count_bidirectional([(1, 2), (2, 1), (1, 2)]), '2')

    def test_invalid_input_type(self):
        self.assertRaises(TypeError, count_bidirectional, 'not a list')

    def test_invalid_input_format(self):
        self.assertRaises(ValueError, count_bidirectional, [(1, 'a'), (2, 3)])
