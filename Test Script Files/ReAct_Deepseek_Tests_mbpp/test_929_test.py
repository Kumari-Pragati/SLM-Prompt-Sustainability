import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):

    def test_typical_case(self):
        tuplex = (1, 2, 3, 4, 5, 2, 3, 2)
        value = 2
        self.assertEqual(count_tuplex(tuplex, value), 3)

    def test_empty_tuplex(self):
        tuplex = ()
        value = 2
        self.assertEqual(count_tuplex(tuplex, value), 0)

    def test_value_not_in_tuplex(self):
        tuplex = (1, 2, 3, 4, 5)
        value = 6
        self.assertEqual(count_tuplex(tuplex, value), 0)

    def test_single_value_tuplex(self):
        tuplex = (2,)
        value = 2
        self.assertEqual(count_tuplex(tuplex, value), 1)

    def test_repeated_value_tuplex(self):
        tuplex = (2, 2, 2, 2)
        value = 2
        self.assertEqual(count_tuplex(tuplex, value), 4)

    def test_large_tuplex(self):
        tuplex = tuple(range(1, 10001))
        value = 5000
        self.assertEqual(count_tuplex(tuplex, value), 1)
