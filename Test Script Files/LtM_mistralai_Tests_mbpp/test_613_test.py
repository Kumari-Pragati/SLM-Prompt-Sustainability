import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(maximum_value([(1, [1, 2, 3]), (2, [4, 5, 6]), (3, [7, 8, 9])]), [(1, 3), (2, 6), (3, 9)])

    def test_empty_input(self):
        self.assertEqual(maximum_value([(1, []), (2, [])]), [(1, None), (2, None)])

    def test_single_list(self):
        self.assertEqual(maximum_value([(1, [1, 2, 3])]), [(1, 3)])

    def test_negative_numbers(self):
        self.assertEqual(maximum_value([(1, [-1, -2, -3]), (2, [-4, -5, -6])]), [(1, -1), (2, -4)])

    def test_maximum_value(self):
        self.assertEqual(maximum_value([(1, [sys.maxsize, -sys.maxsize]), (2, [sys.maxsize, -sys.maxsize, sys.maxsize * 2])]), [(1, sys.maxsize), (2, sys.maxsize * 2)])

    def test_minimum_value(self):
        self.assertEqual(maximum_value([(1, [-sys.maxsize, -sys.maxsize]), (2, [-sys.maxsize, -sys.maxsize, -sys.maxsize * 2])]), [(1, -sys.maxsize), (2, -sys.maxsize * 2)])
