import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(access_elements([1, 2, 3, 4, 5], [0, 1, 3]), [1, 2, 4])

    def test_edge_case_empty_list(self):
        self.assertEqual(access_elements([1, 2, 3, 4, 5], []), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(access_elements([1, 2, 3, 4, 5], [0]), [1])

    def test_edge_case_out_of_range(self):
        with self.assertRaises(IndexError):
        access_elements([1, 2, 3, 4, 5], [0, 1, 5])

    def test_edge_case_negative_index(self):
        with self.assertRaises(IndexError):
        access_elements([1, 2, 3, 4, 5], [0, 1, -1])

    def test_edge_case_non_integer_index(self):
        with self.assertRaises(TypeError):
        access_elements([1, 2, 3, 4, 5], [0, 1, 'a'])

    def test_edge_case_non_list_index(self):
        with self.assertRaises(TypeError):
        access_elements([1, 2, 3, 4, 5], [0, 1, 2, 'a'])
