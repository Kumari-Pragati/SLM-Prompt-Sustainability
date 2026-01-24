import unittest
from mbpp_41_code import filter_evennumbers

class TestFilterEvennumbers(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(filter_evennumbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_edge_case_empty_list(self):
        self.assertEqual(filter_evennumbers([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(filter_evennumbers([3]), [])

    def test_edge_case_single_even_element_list(self):
        self.assertEqual(filter_evennumbers([2]), [2])

    def test_edge_case_multiple_even_elements_list(self):
        self.assertEqual(filter_evennumbers([2, 4, 6]), [2, 4, 6])

    def test_edge_case_multiple_odd_elements_list(self):
        self.assertEqual(filter_evennumbers([1, 3, 5]), [])

    def test_edge_case_mixed_elements_list(self):
        self.assertEqual(filter_evennumbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            filter_evennumbers(123)

    def test_invalid_input_non_integer_list(self):
        with self.assertRaises(TypeError):
            filter_evennumbers(['a', 'b', 'c'])
