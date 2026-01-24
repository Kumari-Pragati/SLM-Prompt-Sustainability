import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(count_tuplex((1, 2, 3, 2, 4, 2), 2), 3)

    def test_empty_tuplex(self):
        self.assertEqual(count_tuplex((), 2), 0)

    def test_value_not_in_tuplex(self):
        self.assertEqual(count_tuplex((1, 2, 3, 4, 5), 6), 0)

    def test_single_value_in_tuplex(self):
        self.assertEqual(count_tuplex((1, 2, 3, 2, 4, 2), 1), 1)

    def test_large_tuplex(self):
        self.assertEqual(count_tuplex(tuple(range(1, 1000001)), 500000), 1)

    def test_negative_values(self):
        self.assertEqual(count_tuplex((-1, -2, -3, -2, -4, -2), -2), 3)

    def test_mixed_types(self):
        self.assertEqual(count_tuplex(('a', 2, 3.0, 2, 'b', 2), 2), 3)
