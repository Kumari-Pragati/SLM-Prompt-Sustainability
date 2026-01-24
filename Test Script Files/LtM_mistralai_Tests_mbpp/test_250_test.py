import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_X((1, 2, 'x', 'x', 'x'), 'x'), 3)
        self.assertEqual(count_X((1, 2, 'X', 'x', 'X'), 'x'), 3)

    def test_empty_input(self):
        self.assertEqual(count_X((), 'x'), 0)

    def test_single_input(self):
        self.assertEqual(count_X(('x',), 'x'), 1)

    def test_min_max_values(self):
        self.assertEqual(count_X((chr(0), chr(255)), 'x'), 0)

    def test_mixed_case(self):
        self.assertEqual(count_X((1, 'X', 3, 'x', 'A', 'X'), 'x'), 2)

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_X, (1, 2, 'x'), 3)
