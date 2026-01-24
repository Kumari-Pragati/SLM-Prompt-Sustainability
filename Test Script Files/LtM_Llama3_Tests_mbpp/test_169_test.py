import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)
        self.assertEqual(get_pell(3), 2)
        self.assertEqual(get_pell(4), 5)
        self.assertEqual(get_pell(5), 8)

    def test_edge(self):
        self.assertEqual(get_pell(0), 0)
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)
        self.assertEqual(get_pell(3), 2)
        self.assertEqual(get_pell(4), 5)
        self.assertEqual(get_pell(5), 8)

    def test_large(self):
        self.assertEqual(get_pell(10), 55)
        self.assertEqual(get_pell(20), 177)
        self.assertEqual(get_pell(30), 610)
