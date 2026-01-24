import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5), 3), 1)

    def test_edge(self):
        self.assertEqual(count_X((1, 2, 2, 4, 5), 2), 2)

    def test_empty(self):
        self.assertEqual(count_X((), 3), 0)

    def test_single(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5), 5), 1)

    def test_no_match(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5), 6), 0)

    def test_multiple_match(self):
        self.assertEqual(count_X((1, 2, 2, 4, 5), 2), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_X("hello", 3)
