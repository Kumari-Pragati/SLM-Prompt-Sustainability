import unittest
from mbpp_105_code import count

class TestCount(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(count([1, 2, 3, 4, 5]), 15)

    def test_edge(self):
        self.assertEqual(count([-1, -2, -3, -4, -5]), -15)

    def test_empty(self):
        self.assertEqual(count([]), 0)

    def test_single(self):
        self.assertEqual(count([10]), 10)

    def test_negative(self):
        self.assertEqual(count([-1, -2, -3, -4, -5]), -15)

    def test_mixed(self):
        self.assertEqual(count([1, -2, 3, -4, 5]), 3)

    def test_large(self):
        self.assertEqual(count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)
