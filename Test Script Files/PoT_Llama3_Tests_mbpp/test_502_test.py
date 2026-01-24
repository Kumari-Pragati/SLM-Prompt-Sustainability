import unittest
from mbpp_502_code import find

class TestFind(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(find(10, 3), 1)

    def test_edge(self):
        self.assertEqual(find(0, 3), 0)
        self.assertEqual(find(3, 3), 0)

    def test_negative(self):
        self.assertEqual(find(-10, 3), -1)

    def test_zero(self):
        self.assertEqual(find(0, 0), 0)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            find('a', 3)
