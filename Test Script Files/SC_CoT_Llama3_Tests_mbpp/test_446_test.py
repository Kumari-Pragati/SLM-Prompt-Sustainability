import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):

    def test_typical_input(self):
        tup = (1, 2, 3)
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(count_Occurrence(tup, lst), 3)

    def test_edge_case_empty_tuple(self):
        tup = ()
        lst = [1, 2, 3]
        self.assertEqual(count_Occurrence(tup, lst), 0)

    def test_edge_case_empty_list(self):
        tup = (1, 2, 3)
        lst = []
        self.assertEqual(count_Occurrence(tup, lst), 0)

    def test_edge_case_single_element_tuple(self):
        tup = (1,)
        lst = [1, 2, 3]
        self.assertEqual(count_Occurrence(tup, lst), 1)

    def test_edge_case_single_element_list(self):
        tup = (1, 2, 3)
        lst = [1]
        self.assertEqual(count_Occurrence(tup, lst), 1)

    def test_edge_case_tuple_and_list_of_same_elements(self):
        tup = (1, 2, 3)
        lst = [1, 2, 3]
        self.assertEqual(count_Occurrence(tup, lst), 3)

    def test_edge_case_tuple_and_list_of_disjoint_elements(self):
        tup = (1, 2, 3)
        lst = [4, 5, 6]
        self.assertEqual(count_Occurrence(tup, lst), 0)

    def test_invalid_input_non_iterable(self):
        tup = 'not a tuple'
        lst = [1, 2, 3]
        with self.assertRaises(TypeError):
            count_Occurrence(tup, lst)

    def test_invalid_input_non_iterable2(self):
        tup = (1, 2, 3)
        lst = 'not a list'
        with self.assertRaises(TypeError):
            count_Occurrence(tup, lst)
