import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):
    def test_typical_use_case(self):
        tuplex = (1, 2, 2, 3, 4, 2)
        value = 2
        self.assertEqual(count_tuplex(tuplex, value), 3)

    def test_edge_case_empty_tuplex(self):
        tuplex = ()
        value = 2
        self.assertEqual(count_tuplex(tuplex, value), 0)

    def test_boundary_case_single_element_tuplex(self):
        tuplex = (2,)
        value = 2
        self.assertEqual(count_tuplex(tuplex, value), 1)

    def test_boundary_case_multiple_same_values(self):
        tuplex = (1, 2, 2, 3, 4, 2, 2)
        value = 2
        self.assertEqual(count_tuplex(tuplex, value), 4)

    def test_error_handling_non_tuple_input(self):
        tuplex = "not a tuple"
        value = 2
        with self.assertRaises(TypeError):
            count_tuplex(tuplex, value)
