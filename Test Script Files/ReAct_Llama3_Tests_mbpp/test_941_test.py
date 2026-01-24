import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_elim([1, 2, 3]), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_elim([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(count_elim([1]), 1)

    def test_edge_case_single_tuple(self):
        self.assertEqual(count_elim([(1, 2)]), 0)

    def test_edge_case_multiple_tuples(self):
        self.assertEqual(count_elim([(1, 2), (3, 4)]), 0)

    def test_edge_case_mixed_types(self):
        self.assertEqual(count_elim([1, 2, (3, 4)]), 2)

    def test_edge_case_mixed_types_break_on_tuple(self):
        self.assertEqual(count_elim([1, 2, (3, 4), 5]), 2)
