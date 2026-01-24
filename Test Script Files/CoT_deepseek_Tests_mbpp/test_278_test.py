import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4)), 4)

    def test_empty_tuple(self):
        self.assertEqual(count_first_elements(()), 0)

    def test_tuple_with_tuples(self):
        self.assertEqual(count_first_elements((1, (2, 3), 4)), 1)

    def test_tuple_with_non_tuples(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4)), 4)

    def test_tuple_with_mixed_types(self):
        self.assertEqual(count_first_elements((1, 'a', 3.0, 4)), 1)

    def test_single_tuple(self):
        self.assertEqual(count_first_elements(((1, 2), 3, 4)), 1)

    def test_tuple_with_nested_tuples(self):
        self.assertEqual(count_first_elements((1, (2, (3, 4)), 5)), 1)

    def test_tuple_with_empty_tuples(self):
        self.assertEqual(count_first_elements(((), 2, 3)), 0)
