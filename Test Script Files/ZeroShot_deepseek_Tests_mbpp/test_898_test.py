import unittest
from mbpp_898_code import groupby
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):

    def test_extract_elements(self):
        self.assertEqual(extract_elements([1, 1, 1, 2, 2, 3, 3, 3, 3], 3), [1, 1, 1, 3, 3, 3, 3])
        self.assertEqual(extract_elements([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4], 4), [4, 4, 4, 4, 4])
        self.assertEqual(extract_elements([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1), [1])
        self.assertEqual(extract_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [])
        self.assertEqual(extract_elements([], 0), [])
