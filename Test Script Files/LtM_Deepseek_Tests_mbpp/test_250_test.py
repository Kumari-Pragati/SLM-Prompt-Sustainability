import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5), 3), 1)

    def test_multiple_occurrences(self):
        self.assertEqual(count_X((1, 2, 3, 3, 4, 5), 3), 2)

    def test_no_occurrences(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5), 6), 0)

    def test_empty_tuple(self):
        self.assertEqual(count_X((), 3), 0)

    def test_large_tuple(self):
        self.assertEqual(count_X((i for i in range(1, 1000001)), 500000), 1)

    def test_negative_numbers(self):
        self.assertEqual(count_X((-1, -2, -3, -4, -5), -3), 1)

    def test_mixed_types(self):
        self.assertEqual(count_X((1, '2', 3.0, 4, '5'), '2'), 1)
