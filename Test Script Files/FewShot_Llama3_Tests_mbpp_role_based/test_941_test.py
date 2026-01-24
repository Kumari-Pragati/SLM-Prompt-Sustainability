import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_elim([1, 2, 3, 4]), 4)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_elim([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(count_elim([1]), 1)

    def test_edge_case_list_with_tuple(self):
        self.assertEqual(count_elim([1, 2, (3, 4)]), 2)

    def test_edge_case_list_with_multiple_tuples(self):
        self.assertEqual(count_elim([1, 2, (3, 4), (5, 6)]), 2)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            count_elim("not a list")
