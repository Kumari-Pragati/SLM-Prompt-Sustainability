import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):

    def test_catalan_number_typical_cases(self):
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)
        self.assertEqual(catalan_number(2), 2)
        self.assertEqual(catalan_number(3), 5)
        self.assertEqual(catalan_number(4), 14)
        self.assertEqual(catalan_number(5), 42)

    def test_catalan_number_edge_cases(self):
        self.assertEqual(catalan_number(-1), 1)
        self.assertEqual(catalan_number(-5), 1)
        self.assertEqual(catalan_number(6), 149)
        self.assertEqual(catalan_number(10), 16796)

    def test_catalan_number_invalid_inputs(self):
        with self.assertRaises(RecursionError):
            catalan_number(1000)
