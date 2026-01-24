import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency([1, 2, 3, 4, 2, 2, 3, 2], 2), 4)

    def test_edge_case_empty_list(self):
        self.assertEqual(frequency([], 2), 0)

    def test_edge_case_no_match(self):
        self.assertEqual(frequency([1, 2, 3, 4], 5), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(frequency([2], 2), 1)
        self.assertEqual(frequency([2], 3), 0)

    def test_error_case_non_list_input(self):
        with self.assertRaises(TypeError):
            frequency(123, 2)

    def test_error_case_non_integer_elements(self):
        with self.assertRaises(TypeError):
            frequency(['a', 'b', 'c'], 'a')
