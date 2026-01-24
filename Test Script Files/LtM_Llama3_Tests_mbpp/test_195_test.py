import unittest
from mbpp_195_code import first

class TestFirstFunction(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 3, 5), 2)
        self.assertEqual(first([1, 2, 3, 4, 5], 1, 5), 0)
        self.assertEqual(first([1, 2, 3, 4, 5], 5, 5), 4)

    def test_edge(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 0, 5), 0)
        self.assertEqual(first([1, 2, 3, 4, 5], 5, 5), 4)
        self.assertEqual(first([1, 2, 3, 4, 5], 1, 1), -1)

    def test_complex(self):
        self.assertEqual(first([1, 2, 3, 4, 5, 6], 3, 6), 2)
        self.assertEqual(first([1, 2, 3, 4, 5, 6], 6, 6), 5)
        self.assertEqual(first([1, 2, 3, 4, 5, 6], 0, 6), 0)
