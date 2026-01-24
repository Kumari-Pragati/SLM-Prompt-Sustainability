import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(concatenate_elements((1, 2, 3)), (3, 4, 5))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(concatenate_elements(()), ())

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(concatenate_elements((1,)), (1,))

    def test_edge_case_two_element_tuple(self):
        self.assertEqual(concatenate_elements((1, 2)), (3,))

    def test_edge_case_three_element_tuple(self):
        self.assertEqual(concatenate_elements((1, 2, 3)), (3, 4, 5))

    def test_edge_case_long_tuple(self):
        self.assertEqual(concatenate_elements((1, 2, 3, 4, 5)), (3, 4, 5, 6, 7))

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            concatenate_elements("not a tuple")
