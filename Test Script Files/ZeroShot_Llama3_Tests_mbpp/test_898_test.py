import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):

    def test_extract_elements(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6], 2), [2, 4, 6])
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7], 2), [2, 4, 6, 7])
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8], 2), [2, 4, 6, 7, 8])
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9], 2), [2, 4, 6, 7, 8, 9])
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10], 2), [2, 4, 6, 7, 8, 9, 10])
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11], 2), [2, 4, 6, 7, 8, 9, 10, 11])
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12], 2), [2, 4, 6, 7, 8, 9, 10, 11, 12])
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13], 2), [2, 4, 6, 7, 8, 9, 10, 11, 12, 13])
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14], 2), [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15], 2), [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8,