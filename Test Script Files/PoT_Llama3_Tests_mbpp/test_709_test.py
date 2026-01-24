import unittest
from mbpp_709_code import get_unique

class TestGetUnique(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(get_unique([["a", 1], ["b", 2], ["c", 3]]), '{"1": 1, "2": 1, "3": 1}')

    def test_edge(self):
        self.assertEqual(get_unique([["a", 1], ["a", 1], ["b", 2], ["c", 3]]), '{"1": 1, "2": 1, "3": 1}')

    def test_edge2(self):
        self.assertEqual(get_unique([["a", 1], ["b", 2], ["c", 3], ["c", 3]]), '{"1": 1, "2": 1, "3": 1}')

    def test_edge3(self):
        self.assertEqual(get_unique([["a", 1], ["a", 1], ["a", 1], ["b", 2], ["c", 3]]), '{"1": 1, "2": 1, "3": 1}')

    def test_edge4(self):
        self.assertEqual(get_unique([["a", 1], ["a", 1], ["a", 1], ["a", 1], ["b", 2], ["c", 3]]), '{"1": 1, "2": 1, "3": 1}')

    def test_edge5(self):
        self.assertEqual(get_unique([["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["b", 2], ["c", 3]]), '{"1": 1, "2": 1, "3": 1}')

    def test_edge6(self):
        self.assertEqual(get_unique([["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["b", 2], ["c", 3]]), '{"1": 1, "2": 1, "3": 1}')

    def test_edge7(self):
        self.assertEqual(get_unique([["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["b", 2], ["c", 3]]), '{"1": 1, "2": 1, "3": 1}')

    def test_edge8(self):
        self.assertEqual(get_unique([["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["b", 2], ["c", 3]]), '{"1": 1, "2": 1, "3": 1}')

    def test_edge9(self):
        self.assertEqual(get_unique([["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["b", 2], ["c", 3]]), '{"1": 1, "2": 1, "3": 1}')

    def test_edge10(self):
        self.assertEqual(get_unique([["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["a", 1], ["b", 2], ["c", 3]]), '{"1": 1, "2": 1, "3": 1}')
