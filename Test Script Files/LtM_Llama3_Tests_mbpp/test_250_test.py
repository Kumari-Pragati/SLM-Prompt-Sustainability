import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_X((1, 2, 3), 1), 1)
        self.assertEqual(count_X((1, 2, 3), 2), 1)
        self.assertEqual(count_X((1, 2, 3), 3), 1)
        self.assertEqual(count_X((1, 2, 3), 4), 0)

    def test_empty(self):
        self.assertEqual(count_X((), 1), 0)

    def test_single_element(self):
        self.assertEqual(count_X((1,), 1), 1)
        self.assertEqual(count_X((1,), 2), 0)

    def test_multiple_elements(self):
        self.assertEqual(count_X((1, 2, 3, 1, 2, 3), 1), 3)
        self.assertEqual(count_X((1, 2, 3, 1, 2, 3), 2), 3)
        self.assertEqual(count_X((1, 2, 3, 1, 2, 3), 3), 3)

    def test_non_integer(self):
        self.assertEqual(count_X((1, 2, 3), 'a'), 0)
