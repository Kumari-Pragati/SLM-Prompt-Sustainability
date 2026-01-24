import unittest
from mbpp_659_code import Repeat

class TestRepeat(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(Repeat([1, 2, 3, 2, 4, 5]), [2])

    def test_edge(self):
        self.assertEqual(Repeat([1, 1, 1, 1]), [1])

    def test_edge2(self):
        self.assertEqual(Repeat([1, 2, 3, 4, 5]), [])

    def test_edge3(self):
        self.assertEqual(Repeat(['a', 'b', 'c', 'd', 'e']), [])

    def test_edge4(self):
        self.assertEqual(Repeat(['a', 'a', 'a', 'a']), ['a'])

    def test_edge5(self):
        self.assertEqual(Repeat(['a', 'b', 'c', 'd', 'e', 'a']), ['a'])

    def test_edge6(self):
        self.assertEqual(Repeat(['a', 'a', 'a', 'a', 'a']), ['a'])

    def test_edge7(self):
        self.assertEqual(Repeat(['a', 'b', 'c', 'd', 'e', 'f']), [])

    def test_edge8(self):
        self.assertEqual(Repeat(['a', 'a', 'a', 'a', 'a', 'a']), ['a'])

    def test_edge9(self):
        self.assertEqual(Repeat(['a', 'b', 'c', 'd', 'e', 'f', 'g']), [])

    def test_edge10(self):
        self.assertEqual(Repeat(['a', 'a', 'a', 'a', 'a', 'a', 'a']), ['a'])
