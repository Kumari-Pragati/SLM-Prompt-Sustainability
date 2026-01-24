import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(get_carol(1), 0)

    def test_small_positive_integer(self):
        self.assertEqual(get_carol(2), 3)

    def test_large_positive_integer(self):
        self.assertEqual(get_carol(5), 476)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            get_carol(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            get_carol('a')

    def test_edge_case_zero(self):
        self.assertEqual(get_carol(0), 0)
