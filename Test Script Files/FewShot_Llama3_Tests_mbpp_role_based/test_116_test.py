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

    def test_non_integer_values(self):
        with self.assertRaises(TypeError):
            tuple_to_int(("a", "b", "c"))
