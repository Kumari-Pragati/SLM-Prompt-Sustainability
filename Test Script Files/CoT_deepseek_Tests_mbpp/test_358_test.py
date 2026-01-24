import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(moddiv_list([10, 20, 30], [3, 5, 7]), [1, 4, 4])

    def test_edge_case_with_zero(self):
        self.assertEqual(moddiv_list([10, 20, 30], [0, 5, 7]), [10, 20, 30])

    def test_boundary_case_with_large_numbers(self):
        self.assertEqual(moddiv_list(list(range(1, 10001)), list(range(1, 10001))), list(range(1, 10001)))

    def test_invalid_input_different_lengths(self):
        with self.assertRaises(ValueError):
            moddiv_list([10, 20, 30], [3, 5])

    def test_invalid_input_non_integer_elements(self):
        with self.assertRaises(TypeError):
            moddiv_list([10, 20, 30.5], [3, 5, 7])

    def test_invalid_input_empty_lists(self):
        self.assertEqual(moddiv_list([], []), [])
