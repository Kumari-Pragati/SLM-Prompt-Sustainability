import unittest
from mbpp_317_code import modified_encode

class TestModifiedEncode(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(modified_encode(['a', 'a', 'b', 'b', 'c']), [[2, 'a'], [2, 'b'], 'c'])

    def test_single_element(self):
        self.assertEqual(modified_encode(['a']), ['a'])

    def test_empty_list(self):
        self.assertEqual(modified_encode([]), [])

    def test_repeated_elements(self):
        self.assertEqual(modified_encode(['a', 'a', 'a']), [[3, 'a']])

    def test_single_repeated_element(self):
        self.assertEqual(modified_encode(['a', 'a']), [[2, 'a']])

    def test_mixed_case(self):
        self.assertEqual(modified_encode(['a', 'A', 'a']), [[2, 'a'], 'A'])

    def test_numeric_elements(self):
        self.assertEqual(modified_encode([1, 1, 2, 2]), [[2, 1], [2, 2]])

    def test_negative_numbers(self):
        self.assertEqual(modified_encode([-1, -1, -2, -2]), [[2, -1], [2, -2]])

    def test_mixed_numeric_and_string(self):
        self.assertEqual(modified_encode(['a', 1, 1, 'a']), [[2, 'a'], [2, 1]])
