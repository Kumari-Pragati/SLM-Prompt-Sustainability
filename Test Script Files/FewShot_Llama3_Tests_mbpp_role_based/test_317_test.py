import unittest
from mbpp_317_code import modified_encode

class TestModifiedEncode(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(modified_encode([]), [])

    def test_single_element_list(self):
        self.assertEqual(modified_encode([1]), [[1]])

    def test_multiple_elements_list(self):
        self.assertEqual(modified_encode([1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 5]), [[2, 1], [3, 3], [1, 4], [4, 5]])

    def test_list_with_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]), [[2, 1], [2, 2], [3, 3], [1, 4], [3, 5]])

    def test_list_with_empty_sublist(self):
        self.assertEqual(modified_encode([1, 1, 2, 2, 3, 3, 3, 4, '', 5, 5, 5]), [[2, 1], [2, 2], [3, 3], [1, 4], [1, 5]])
