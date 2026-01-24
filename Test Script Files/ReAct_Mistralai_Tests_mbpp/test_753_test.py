import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(min_k([], 1), [])

    def test_single_element(self):
        self.assertListEqual(min_k([(1, 1)], 1), [(1, 1)])
        self.assertListEqual(min_k([(1, 1)], 2), [(1, 1)])

    def test_multiple_elements(self):
        self.assertListEqual(min_k([(1, 1), (2, 2), (3, 3), (4, 4)], 2), [(1, 1), (2, 2)])
        self.assertListEqual(min_k([(1, 1), (2, 2), (3, 3), (4, 4)], 4), [(1, 1), (2, 2), (3, 3), (4, 4)])

    def test_duplicates(self):
        self.assertListEqual(min_k([(1, 1), (1, 2), (2, 2), (3, 3)], 2), [(1, 1), (1, 2)])

    def test_negative_k(self):
        with self.assertRaises(ValueError):
            min_k([(1, 1), (2, 2)], -1)

    def test_list_with_only_key_error(self):
        with self.assertRaises(TypeError):
            min_k([1, 2], 1)
