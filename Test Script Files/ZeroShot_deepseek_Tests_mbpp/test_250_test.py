import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):

    def test_count_X_positive(self):
        self.assertEqual(count_X((1, 2, 3, 'X', 4, 'X'), 'X'), 2)

    def test_count_X_negative(self):
        self.assertEqual(count_X((1, 2, 3, 'Y', 4, 'X'), 'X'), 1)

    def test_count_X_empty(self):
        self.assertEqual(count_X((), 'X'), 0)

    def test_count_X_no_X(self):
        self.assertEqual(count_X((1, 2, 3, 4), 'X'), 0)
