import unittest
from mbpp_321_code import find_demlo

class TestFindDemlo(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(find_demlo("abc"), "123456789abc987654321")

    def test_empty_string(self):
        self.assertEqual(find_demlo(""), "")

    def test_single_character(self):
        self.assertEqual(find_demlo("a"), "1231a123")

    def test_edge_case_zero_length(self):
        self.assertEqual(find_demlo(""), "")

    def test_edge_case_single_character(self):
        self.assertEqual(find_demlo("a"), "1231a123")

    def test_edge_case_empty_string(self):
        self.assertEqual(find_demlo(""), "")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            find_demlo(123)

    def test_invalid_input_non_string_list(self):
        with self.assertRaises(TypeError):
            find_demlo([1, 2, 3])

    def test_invalid_input_non_string_tuple(self):
        with self.assertRaises(TypeError):
            find_demlo((1, 2, 3))
