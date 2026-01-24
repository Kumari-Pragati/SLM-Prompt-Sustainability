import unittest
from mbpp_363_code import add_K_element

class TestAddKElement(unittest.TestCase):

    def test_add_K_element(self):
        self.assertEqual(add_K_element([[1, 2], [3, 4]], 5), [[6, 7], [8, 9]])
        self.assertEqual(add_K_element([[1, 2, 3], [4, 5, 6]], 7), [[8, 9, 10], [11, 12, 13]])
        self.assertEqual(add_K_element([[1, 2], [3, 4, 5]], 6), [[7, 8], [9, 10, 11]])
        self.assertEqual(add_K_element([[1, 2, 3, 4], [5, 6, 7, 8]], 9), [[10, 11, 12, 13], [14, 15, 16, 17]])
        self.assertEqual(add_K_element([[1, 2], [3, 4]], 0), [[1, 2], [3, 4]])

    def test_add_K_element_empty_list(self):
        self.assertEqual(add_K_element([], 5), [])

    def test_add_K_element_single_element(self):
        self.assertEqual(add_K_element([[1, 2, 3, 4, 5]], 6), [[7, 8, 9, 10, 11]])
