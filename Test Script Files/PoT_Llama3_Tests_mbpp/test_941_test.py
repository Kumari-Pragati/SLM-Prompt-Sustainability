import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_elim([1, 2, 3]), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_elim([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(count_elim([1]), 1)

    def test_edge_case_single_tuple_element_list(self):
        self.assertEqual(count_elim([(1,)]), 0)

    def test_edge_case_multiple_tuple_element_list(self):
        self.assertEqual(count_elim([(1,), (2,), (3,)]), 0)

    def test_edge_case_list_with_non_integer_elements(self):
        self.assertEqual(count_elim([1, 'a', 3]), 3)

    def test_edge_case_list_with_non_integer_and_tuple_elements(self):
        self.assertEqual(count_elim([1, 'a', (2,), 3]), 3)
