import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_tuples((1, 2, 3), {1, 2, 3}))

    def test_edge_case_empty_tuple(self):
        self.assertTrue(check_tuples((), {}))

    def test_edge_case_empty_set(self):
        self.assertTrue(check_tuples((1,), {}))

    def test_edge_case_single_element(self):
        self.assertTrue(check_tuples((1,), {1}))

    def test_edge_case_single_element_set(self):
        self.assertTrue(check_tuples({1}, {1}))

    def test_edge_case_single_element_not_in_set(self):
        self.assertFalse(check_tuples((1,), {2}))

    def test_edge_case_set_with_extra_elements(self):
        self.assertFalse(check_tuples((1, 2, 3), {1, 2, 4}))

    def test_invalid_input_tuple_not_iterable(self):
        with self.assertRaises(TypeError):
            check_tuples('not a tuple', {1, 2, 3})

    def test_invalid_input_set_not_iterable(self):
        with self.assertRaises(TypeError):
            check_tuples((1, 2, 3), 'not a set')
