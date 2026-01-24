import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1, 2, 3]), 3)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(count_Occurrence((), [1, 2, 3]), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_Occurrence((1, 2, 3), []), 0)

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(count_Occurrence((1), [1, 2, 3]), 1)

    def test_edge_case_single_element_list(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1]), 1)

    def test_edge_case_tuple_and_list_of_same_elements(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1, 2, 3]), 3)

    def test_edge_case_tuple_and_list_of_disjoint_elements(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [4, 5, 6]), 0)

    def test_edge_case_tuple_and_list_of_overlapping_elements(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1, 2, 4, 5]), 2)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            count_Occurrence("hello", [1, 2, 3])

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            count_Occurrence((1, 2, 3), "hello")
