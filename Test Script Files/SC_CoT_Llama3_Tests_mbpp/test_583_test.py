import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)
        self.assertEqual(catalan_number(2), 2)
        self.assertEqual(catalan_number(3), 5)
        self.assertEqual(catalan_number(4), 14)

    def test_edge_cases(self):
        self.assertEqual(catalan_number(-1), 1)
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)
        self.assertEqual(catalan_number(2), 2)
        self.assertEqual(catalan_number(3), 5)

    def test_large_numbers(self):
        self.assertEqual(catalan_number(5), 42)
        self.assertEqual(catalan_number(6), 132)
        self.assertEqual(catalan_number(7), 429)
        self.assertEqual(catalan_number(8), 1430)
        self.assertEqual(catalan_number(9), 4862)

    def test_invalid_inputs(self):
        with self.assertRaises RecursionError:
            catalan_number(10**100)
