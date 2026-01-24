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
        self.assertEqual(catalan_number(5), 42)

    def test_catalan_number_large_numbers(self):
        self.assertEqual(catalan_number(10), 742)
        self.assertEqual(catalan_number(11), 6435)
        self.assertEqual(catalan_number(12), 132096)
        self.assertEqual(catalan_number(13), 533712640)

    def test_catalan_number_invalid_input(self):
        with self.assertRaises(TypeError):
            catalan_number(-1)
        with self.assertRaises(TypeError):
            catalan_number(2.5)
