import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(min_k([], 1), [])

    def test_single_element(self):
        self.assertListEqual(min_k([(1, 1)], 1), [(1, 1)])

    def test_multiple_elements(self):
        self.assertListEqual(min_k([(1, 1), (2, 2), (3, 3), (4, 4)], 2), [(1, 1), (2, 2)])

    def test_k_greater_than_length(self):
        self.assertListEqual(min_k([(1, 1), (2, 2), (3, 3), (4, 4)], 5), [(1, 1), (2, 2), (3, 3), (4, 4)])

    def test_k_equal_to_length(self):
        self.assertListEqual(min_k([(1, 1), (2, 2), (3, 3), (4, 4)], 4), [(1, 1), (2, 2), (3, 3), (4, 4)])

    def test_duplicate_elements(self):
        self.assertListEqual(min_k([(1, 1), (1, 1), (2, 2), (3, 3), (4, 4)], 2), [(1, 1), (2, 2)])

    def test_invalid_k_type(self):
        with self.assertRaises(TypeError):
            min_k([(1, 1), (2, 2), (3, 3), (4, 4)], 'K')

    def test_invalid_list_type(self):
        with self.assertRaises(TypeError):
            min_k('test_list', 1)
