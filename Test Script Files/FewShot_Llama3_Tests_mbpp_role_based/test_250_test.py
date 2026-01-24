import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):
    def test_count_X_typical_use_case(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5), 3), 1)

    def test_count_X_edge_case(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5), 5), 1)

    def test_count_X_multiple_occurrences(self):
        self.assertEqual(count_X((1, 2, 2, 3, 4, 2), 2), 3)

    def test_count_X_no_occurrences(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5), 6), 0)

    def test_count_X_empty_tuple(self):
        self.assertEqual(count_X((), 1), 0)

    def test_count_X_non_integer_input(self):
        with self.assertRaises(TypeError):
            count_X((1, 2, 3, 4, 5), 'x')
