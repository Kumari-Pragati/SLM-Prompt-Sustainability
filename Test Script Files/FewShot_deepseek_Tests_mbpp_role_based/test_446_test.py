import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a', 'b', 'c']), 3)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(count_Occurrence((), ['a', 'b', 'c']), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), []), 0)

    def test_boundary_case_all_elements_in_tuple_are_in_list(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a', 'b', 'c', 'd']), 3)

    def test_boundary_case_all_elements_in_list_are_in_tuple(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c', 'd'), ['a', 'b', 'c']), 3)

    def test_boundary_case_some_elements_in_tuple_are_in_list(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c', 'd'), ['a', 'b']), 2)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            count_Occurrence('abc', ['a', 'b', 'c'])
