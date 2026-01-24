import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):
    def test_min_length(self):
        self.assertEqual(min_length([1, 2, 3]), (1, 1))
        self.assertEqual(min_length(['a', 'b', 'c']), (1, 'a'))
        self.assertEqual(min_length([1, 2, 3, 4, 5]), (1, 1))
        self.assertEqual(min_length(['a', 'b', 'c', 'd', 'e']), (1, 'a'))
        self.assertEqual(min_length([]), (0, None))
        self.assertEqual(min_length([1]), (1, 1))
        self.assertEqual(min_length(['a']), (1, 'a'))

    def test_min_length_edge_cases(self):
        self.assertEqual(min_length([1, 2, 3, 4, 5, 6]), (1, 1))
        self.assertEqual(min_length(['a', 'b', 'c', 'd', 'e', 'f']), (1, 'a'))
        self.assertEqual(min_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), (1, 1))
        self.assertEqual(min_length(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']), (1, 'a'))

    def test_min_length_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_length(None)
        with self.assertRaises(TypeError):
            min_length('')
