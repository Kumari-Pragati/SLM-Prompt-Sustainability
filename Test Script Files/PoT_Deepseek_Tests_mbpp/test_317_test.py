import unittest
from mbpp_317_code import modified_encode

class TestModifiedEncode(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(modified_encode(['a', 'a', 'b', 'b', 'c', 'c', 'c']), 
                         [[2, 'a'], [2, 'b'], [3, 'c']])

    def test_single_element(self):
        self.assertEqual(modified_encode(['a']), ['a'])

    def test_empty_list(self):
        self.assertEqual(modified_encode([]), [])

    def test_repeated_elements(self):
        self.assertEqual(modified_encode(['a', 'a', 'a']), [[3, 'a']])

    def test_single_repeated_elements(self):
        self.assertEqual(modified_encode(['a', 'a']), [[2, 'a']])

    def test_mixed_elements(self):
        self.assertEqual(modified_encode(['a', 'b', 'c', 'a', 'b', 'c', 'c']), 
                         [[1, 'a'], [1, 'b'], [1, 'c'], [2, 'a'], [2, 'b'], [3, 'c']])
