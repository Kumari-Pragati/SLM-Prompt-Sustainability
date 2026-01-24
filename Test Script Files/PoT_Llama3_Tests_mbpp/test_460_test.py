import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(Extract([[1, 2], [3, 4], [5, 6]]), [1, 3, 5])

    def test_edge(self):
        self.assertEqual(Extract([[1, 2], [3, 4]]), [1, 3])

    def test_empty(self):
        self.assertEqual(Extract([]), [])

    def test_single(self):
        self.assertEqual(Extract([[1, 2]]), [1])

    def test_single_empty(self):
        self.assertEqual(Extract([[]]), [])

    def test_single_single(self):
        self.assertEqual(Extract([[1]]), [1])
