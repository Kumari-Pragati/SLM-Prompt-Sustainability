import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):
    def test_catalan_number_base_case(self):
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)

    def test_catalan_number_small_numbers(self):
        self.assertEqual(catalan_number(2), 2)
        self.assertEqual(catalan_number(3), 5)
        self.assertEqual(catalan_number(4), 14)

    def test_catalan_number_larger_numbers(self):
        self.assertEqual(catalan_number(5), 42)
        self.assertEqual(catalan_number(6), 132)
        self.assertEqual(catalan_number(7), 429)

    def test_catalan_number_invalid_input(self):
        with self.assertRaises RecursionError:
            catalan_number(1000)
