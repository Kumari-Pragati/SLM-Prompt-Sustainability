import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)
        self.assertEqual(catalan_number(2), 2)
        self.assertEqual(catalan_number(3), 5)
        self.assertEqual(catalan_number(4), 14)

    def test_edge(self):
        self.assertEqual(catalan_number(-1), 1)
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)
        self.assertEqual(catalan_number(2), 2)

    def test_large(self):
        self.assertEqual(catalan_number(5), 42)
        self.assertEqual(catalan_number(6), 132)
        self.assertEqual(catalan_number(7), 429)

    def test_invalid(self):
        with self.assertRaisesRecursionLimitError:
            catalan_number(1000)
