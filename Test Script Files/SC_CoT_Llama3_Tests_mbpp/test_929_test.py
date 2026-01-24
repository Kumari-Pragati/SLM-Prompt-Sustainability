import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):
    def test_typical_input(self):
        tuplex = (1, 2, 2, 3, 4, 2)
        value = 2
        self.assertEqual(count_tuplex(tuplex, value), 3)

    def test_edge_case_empty_tuplex(self):
        tuplex = ()
        value = 2
        self.assertEqual(count_tuplex(tuplex, value), 0)

    def test_edge_case_empty_value(self):
        tuplex = (1, 2, 2, 3, 4, 2)
        value = ''
        self.assertEqual(count_tuplex(tuplex, value), 0)

    def test_edge_case_single_element_tuplex(self):
        tuplex = (1,)
        value = 1
        self.assertEqual(count_tuplex(tuplex, value), 1)

    def test_edge_case_single_element_value(self):
        tuplex = (1, 2, 2, 3, 4, 2)
        value = 1
        self.assertEqual(count_tuplex(tuplex, value), 1)

    def test_edge_case_all_elements_match(self):
        tuplex = (1, 1, 1, 1, 1, 1)
        value = 1
        self.assertEqual(count_tuplex(tuplex, value), 6)

    def test_edge_case_no_elements_match(self):
        tuplex = (1, 2, 3, 4, 5, 6)
        value = 7
        self.assertEqual(count_tuplex(tuplex, value), 0)

    def test_invalid_input_non_iterable(self):
        tuplex ='string'
        value = 2
        with self.assertRaises(TypeError):
            count_tuplex(tuplex, value)

    def test_invalid_input_non_integer(self):
        tuplex = (1, 2, 2, 3, 4, 2)
        value ='string'
        with self.assertRaises(TypeError):
            count_tuplex(tuplex, value)
