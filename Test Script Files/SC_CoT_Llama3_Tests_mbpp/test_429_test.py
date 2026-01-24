import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(and_tuples((1, 2, 3), (4, 5, 6)), (0, 3, 6))

    def test_edge_case_empty_input(self):
        self.assertEqual(and_tuples((), (1, 2, 3)), ())

    def test_edge_case_single_element_input(self):
        self.assertEqual(and_tuples((1,), (2,)), (0,))

    def test_edge_case_single_element_input_empty(self):
        self.assertEqual(and_tuples((1,), ()), ())

    def test_edge_case_single_element_input_single_element(self):
        self.assertEqual(and_tuples((1,), (1,)), (1,))

    def test_edge_case_single_element_input_single_element_empty(self):
        self.assertEqual(and_tuples((1,), ()), ())

    def test_edge_case_single_element_input_empty_single_element(self):
        self.assertEqual(and_tuples((), (1,)), ())

    def test_edge_case_single_element_input_empty_single_element_empty(self):
        self.assertEqual(and_tuples((), ()), ())

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            and_tuples("test", (1, 2, 3))

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            and_tuples((1, 2, 3), "test")

    def test_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            and_tuples("test", "test")
