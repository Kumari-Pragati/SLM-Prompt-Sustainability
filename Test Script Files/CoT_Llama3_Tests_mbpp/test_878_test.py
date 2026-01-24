import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_tuples((1, 2, 3), [1, 2, 3]))

    def test_edge_case_empty_tuple(self):
        self.assertFalse(check_tuples((), [1, 2, 3]))

    def test_edge_case_empty_set(self):
        self.assertFalse(check_tuples((1, 2, 3), []))

    def test_edge_case_single_element_tuple(self):
        self.assertTrue(check_tuples((1,), [1]))

    def test_edge_case_single_element_set(self):
        self.assertFalse(check_tuples((1,), []))

    def test_edge_case_tuple_with_duplicates(self):
        self.assertTrue(check_tuples((1, 1, 2), [1, 2]))

    def test_edge_case_set_with_duplicates(self):
        self.assertFalse(check_tuples((1, 1, 2), [1]))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_tuples("test", [1, 2, 3])

    def test_invalid_input_type_set(self):
        with self.assertRaises(TypeError):
            check_tuples((1, 2, 3), "test")
