import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_elim([1, 2, 3, 4, 5]), 5)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_elim([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(count_elim([1]), 1)

    def test_edge_case_single_tuple(self):
        self.assertEqual(count_elim([1, (2, 3)]), 1)

    def test_edge_case_multiple_tuples(self):
        self.assertEqual(count_elim([1, (2, 3), 4, (5, 6)]), 3)

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            count_elim("hello")

    def test_invalid_input_non_iterable_empty_string(self):
        with self.assertRaises(TypeError):
            count_elim("")

    def test_invalid_input_non_iterable_integer(self):
        with self.assertRaises(TypeError):
            count_elim(123)
