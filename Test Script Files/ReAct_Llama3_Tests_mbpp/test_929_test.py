import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):

    def test_typical_case(self):
        tuplex = (1, 2, 3, 2, 1)
        value = 2
        self.assertEqual(count_tuplex(tuplex, value), 2)

    def test_edge_case_empty_tuplex(self):
        tuplex = ()
        value = 1
        self.assertEqual(count_tuplex(tuplex, value), 0)

    def test_edge_case_empty_value(self):
        tuplex = (1, 2, 3, 2, 1)
        value = ''
        self.assertEqual(count_tuplex(tuplex, value), 0)

    def test_edge_case_value_not_in_tuplex(self):
        tuplex = (1, 2, 3, 2, 1)
        value = 4
        self.assertEqual(count_tuplex(tuplex, value), 0)

    def test_edge_case_value_in_tuplex_multiple_times(self):
        tuplex = (1, 2, 2, 3, 2, 1)
        value = 2
        self.assertEqual(count_tuplex(tuplex, value), 3)

    def test_edge_case_value_in_tuplex_first(self):
        tuplex = (2, 1, 3, 2, 1)
        value = 2
        self.assertEqual(count_tuplex(tuplex, value), 1)

    def test_edge_case_value_in_tuplex_last(self):
        tuplex = (1, 2, 3, 2, 1)
        value = 1
        self.assertEqual(count_tuplex(tuplex, value), 1)
