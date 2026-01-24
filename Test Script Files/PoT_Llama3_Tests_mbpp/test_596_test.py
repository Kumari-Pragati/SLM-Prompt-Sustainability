import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tuple_size(()), 24)
        self.assertEqual(tuple_size((1,)), 28)
        self.assertEqual(tuple_size((1, 2)), 32)
        self.assertEqual(tuple_size((1, 2, 3)), 40)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(tuple_size(()), 24)

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(tuple_size((1,)), 28)

    def test_edge_case_tuple_with_multiple_elements(self):
        self.assertEqual(tuple_size((1, 2, 3)), 40)

    def test_edge_case_tuple_with_large_number_of_elements(self):
        self.assertEqual(tuple_size(tuple(range(100))), 136)

    def test_edge_case_tuple_with_mixed_types(self):
        self.assertEqual(tuple_size((1, 'a', 3.14)), 44)

    def test_edge_case_tuple_with_nested_tuples(self):
        self.assertEqual(tuple_size(((1, 2), 3)), 52)
