import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(add_consecutive_nums([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(add_consecutive_nums([1]), [])

    def test_edge_case_two_element_list(self):
        self.assertEqual(add_consecutive_nums([1, 2]), [])

    def test_edge_case_three_element_list(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3]), [1])

    def test_edge_case_last_element(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4]), [1, 3])

    def test_edge_case_first_element(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5]), [1, 3])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            add_consecutive_nums('abc')

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            add_consecutive_nums([1, '2', 3])
