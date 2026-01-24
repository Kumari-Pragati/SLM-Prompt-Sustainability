import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):
    def test_positive_count(self):
        self.assertEqual(count_X((1, 2, 'x', 'x', 'y'), 'x'), 2)

    def test_empty_list(self):
        self.assertEqual(count_X([], 'x'), 0)

    def test_single_element(self):
        self.assertEqual(count_X(('x',), 'x'), 1)

    def test_negative_count(self):
        self.assertEqual(count_X((1, 2, 'y', 'y'), 'x'), 0)

    def test_non_string_element(self):
        self.assertEqual(count_X((1, 2, 3), 'x'), 0)
