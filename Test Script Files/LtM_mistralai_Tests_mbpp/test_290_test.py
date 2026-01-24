import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_length([1, 2, 3]), (3, 3))
        self.assertEqual(max_length(['a', 'b', 'c']), (3, 'c'))

    def test_edge_cases(self):
        self.assertEqual(max_length([1]), (1, 1))
        self.assertEqual(max_length([1, 2]), (2, 2))
        self.assertEqual(max_length([1, 2, 3, 4]), (4, 4))
        self.assertEqual(max_length(['a', 'b', 'c', 'd']), (4, 'd'))
        self.assertEqual(max_length([]), (0, None))

    def test_complex(self):
        self.assertEqual(max_length([1, 2, 3, 4, 5]), (5, 5))
        self.assertEqual(max_length(['a', 'b', 'c', 'd', 'e']), (5, 'e'))
        self.assertEqual(max_length([1, 2, 3, 4, 5, 6]), (6, 6))
        self.assertEqual(max_length(['a', 'b', 'c', 'd', 'e', 'f']), (6, 'f'))
        self.assertEqual(max_length([1, 2, 3, 4, 5, 6, 7]), (7, 7))
        self.assertEqual(max_length(['a', 'b', 'c', 'd', 'e', 'f', 'g']), (7, 'g'))
