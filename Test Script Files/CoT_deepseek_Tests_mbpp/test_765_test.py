import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(is_polite(10), 12)

    def test_large_number(self):
        self.assertEqual(is_polite(1000), 1025)

    def test_small_number(self):
        self.assertEqual(is_polite(1), 2)

    def test_edge_case_zero(self):
        self.assertEqual(is_polite(0), 1)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            is_polite(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            is_polite(1.5)
