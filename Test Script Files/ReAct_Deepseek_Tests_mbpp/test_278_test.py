import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4)), 1)

    def test_typical_case_with_nested_tuples(self):
        self.assertEqual(count_first_elements((1, (2, 3), 4)), 2)

    def test_typical_case_with_mixed_types(self):
        self.assertEqual(count_first_elements((1, '2', 3, 4)), 1)

    def test_empty_tuple(self):
        self.assertEqual(count_first_elements(()), 0)

    def test_tuple_with_single_element(self):
        self.assertEqual(count_first_elements((1,)), 1)

    def test_tuple_with_single_tuple(self):
        self.assertEqual(count_first_elements((('a',),)), 1)

    def test_tuple_with_nested_tuples_and_single_tuple(self):
        self.assertEqual(count_first_elements((1, (2, 3), ('a',))), 2)

    def test_tuple_with_single_tuple_and_single_element(self):
        self.assertEqual(count_first_elements((('a',), 1)), 1)

    def test_tuple_with_single_tuple_and_multiple_elements(self):
        self.assertEqual(count_first_elements((('a',), 1, 2, 3)), 1)

    def test_tuple_with_multiple_nested_tuples(self):
        self.assertEqual(count_first_elements((1, (2, (3, 4)), 5)), 2)

    def test_tuple_with_multiple_nested_tuples_and_single_tuple(self):
        self.assertEqual(count_first_elements((1, (2, (3, 4)), ('a',))), 2)

    def test_tuple_with_multiple_nested_tuples_and_multiple_elements(self):
        self.assertEqual(count_first_elements((1, (2, (3, 4)), 5, 6)), 2)

    def test_tuple_with_multiple_nested_tuples_and_multiple_elements_and_single_tuple(self):
        self.assertEqual(count_first_elements((1, (2, (3, 4)), 5, 6, ('a',))), 2)
