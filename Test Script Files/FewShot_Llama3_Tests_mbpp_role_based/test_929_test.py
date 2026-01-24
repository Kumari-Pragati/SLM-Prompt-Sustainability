import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):
    def test_typical_use_case(self):
        tuplex = (1, 2, 3, 2, 4, 2, 5)
        value = 2
        self.assertEqual(count_tuplex(tuplex, value), 3)

    def test_edge_case_empty_tuplex(self):
        tuplex = ()
        value = 1
        self.assertEqual(count_tuplex(tuplex, value), 0)

    def test_edge_case_single_element_tuplex(self):
        tuplex = (1,)
        value = 1
        self.assertEqual(count_tuplex(tuplex, value), 1)

    def test_edge_case_single_element_tuplex_with_non_existent_value(self):
        tuplex = (1,)
        value = 2
        self.assertEqual(count_tuplex(tuplex, value), 0)

    def test_edge_case_tuplex_with_non_existent_value(self):
        tuplex = (1, 2, 3, 4, 5)
        value = 6
        self.assertEqual(count_tuplex(tuplex, value), 0)
