import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(tuple_to_int(()), 0)

    def test_single_element_tuple(self):
        self.assertEqual(tuple_to_int((1,)), 1)

    def test_multiple_elements_tuple(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)

    def test_negative_numbers(self):
        self.assertEqual(tuple_to_int((-1, -2, -3)), -123)

    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(tuple_to_int((1, -2, 3)), 13)

    def test_zero_in_the_middle(self):
        self.assertEqual(tuple_to_int((1, 0, 3)), 103)

    def test_zero_at_the_end(self):
        self.assertEqual(tuple_to_int((1, 2, 0)), 120)

    def test_zero_at_the_start(self):
        self.assertEqual(tuple_to_int((0, 2, 3)), 23)

    def test_zero_as_the_only_element(self):
        self.assertEqual(tuple_to_int((0,)), 0)

    def test_tuple_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            tuple_to_int((1, 'a', 3))
