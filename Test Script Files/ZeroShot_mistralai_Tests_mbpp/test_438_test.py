import unittest
from mbpp_438_code import count_bidirectional

class TestCountBidirectional(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_bidirectional([]), '0')

    def test_single_element(self):
        self.assertEqual(count_bidirectional([(1, 1)]), '0')

    def test_simple_list(self):
        self.assertEqual(count_bidirectional([(1, 2), (2, 3), (3, 1)]), '1')

    def test_complex_list(self):
        self.assertEqual(count_bidirectional([(1, 2), (2, 3), (3, 4), (4, 1), (2, 1)]), '2')
