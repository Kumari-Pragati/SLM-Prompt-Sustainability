import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5]), [3, 5, 7])

    def test_edge_case_single_element(self):
        self.assertEqual(add_consecutive_nums([1]), [])

    def test_edge_case_empty_list(self):
        self.assertEqual(add_consecutive_nums([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(add_consecutive_nums([1, 1]), [])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            add_consecutive_nums("abc")

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            add_consecutive_nums([1, "a", 3])

    def test_invalid_input_non_consecutive(self):
        with self.assertRaises(TypeError):
            add_consecutive_nums([1, 2, 3, 5, 6])
