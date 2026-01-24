import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(min_k([], 1), [])

    def test_single_element(self):
        self.assertListEqual(min_k([(1, 1)], 1), [(1, 1)])

    def test_multiple_elements(self):
        self.assertListEqual(min_k([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], 3), [(1, 1), (2, 2), (3, 3)])

    def test_K_greater_than_length(self):
        self.assertListEqual(min_k([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], 6), [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])

    def test_negative_K(self):
        self.assertRaises(ValueError, min_k, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], -1)
