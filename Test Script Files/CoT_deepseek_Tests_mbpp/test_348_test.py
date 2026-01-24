import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_ways(4), 1)

    def test_odd_number(self):
        self.assertEqual(find_ways(5), 1)

    def test_large_number(self):
        self.assertEqual(find_ways(10), 45)

    def test_zero(self):
        self.assertEqual(find_ways(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            find_ways(-5)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            find_ways(2.5)

    def test_large_number_with_odd_input(self):
        self.assertEqual(find_ways(11), 1155)
