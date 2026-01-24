import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(zip_tuples((1, 2, 3), (4, 5, 6)), [(3, 4), (2, 5), (1, 6)])

    def test_edge_case_single_tuple(self):
        self.assertEqual(zip_tuples((1, 2, 3), ()), [])

    def test_edge_case_empty_tuples(self):
        self.assertEqual(zip_tuples((), ()), [])

    def test_edge_case_single_element_tuples(self):
        self.assertEqual(zip_tuples((1), (2)), [(1, 2)])

    def test_edge_case_single_element_tuples_reverse(self):
        self.assertEqual(zip_tuples((1), (2, 3)), [(1, 2), (1, 3)])

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            zip_tuples(1, (2, 3))

    def test_invalid_input_non_tuple_reverse(self):
        with self.assertRaises(TypeError):
            zip_tuples((1, 2), 'test')
