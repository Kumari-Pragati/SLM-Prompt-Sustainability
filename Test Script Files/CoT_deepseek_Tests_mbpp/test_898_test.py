import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 1, 1], 2), [1, 1, 2, 2, 3, 3])

    def test_single_element(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 1, 1], 1), [])

    def test_no_elements(self):
        self.assertEqual(extract_elements([], 2), [])

    def test_n_greater_than_length(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 1, 1], 10), [])

    def test_n_equal_to_zero(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 1, 1], 0), [])

    def test_negative_n(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 1, 1], -1), [])

    def test_non_integer_elements(self):
        self.assertEqual(extract_elements(['a', 'a', 'b', 'b', 'c', 'c', 'a', 'a'], 2), ['a', 'a', 'b', 'b', 'c', 'c'])

    def test_mixed_types(self):
        self.assertEqual(extract_elements([1, 'a', 1, 'a', 2, 2, 3, 3], 2), [1, 'a', 1, 'a', 2, 2, 3, 3])
