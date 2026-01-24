import unittest
from mbpp_317_code import modified_encode

class TestModifiedEncode(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(modified_encode([1, 1, 1, 2, 2, 3]), [[3, 1], 2, [2, 2], 3])

    def test_single_element(self):
        self.assertEqual(modified_encode([1]), [1])

    def test_empty_list(self):
        self.assertEqual(modified_encode([]), [])

    def test_repeated_elements(self):
        self.assertEqual(modified_encode(['a', 'a', 'b', 'b', 'c']), [[2, 'a'], ['b', 'b'], 'c'])

    def test_single_repeated_element(self):
        self.assertEqual(modified_encode(['a', 'a']), [[2, 'a']])

    def test_no_repeated_elements(self):
        self.assertEqual(modified_encode(['a', 'b', 'c']), ['a', 'b', 'c'])

    def test_negative_numbers(self):
        self.assertEqual(modified_encode([-1, -1, 1, 1]), [[2, -1], 1])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            modified_encode([1, 'a', 2, 'b'])
