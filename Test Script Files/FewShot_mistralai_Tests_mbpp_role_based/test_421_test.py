import unittest
from mbpp_421_code import concatenate_tuple

class TestConcatenateTuple(unittest.TestCase):
    def test_concatenate_single_element_tuple(self):
        self.assertEqual(concatenate_tuple((1)), "1")

    def test_concatenate_two_element_tuple(self):
        self.assertEqual(concatenate_tuple((1, 2)), "1-2")

    def test_concatenate_three_element_tuple(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), "1-2-3")

    def test_concatenate_empty_tuple(self):
        self.assertEqual(concatenate_tuple(()), "")

    def test_concatenate_tuple_with_negative_numbers(self):
        self.assertEqual(concatenate_tuple((-1, 0, 1)), "-1-0-1")

    def test_concatenate_tuple_with_floats(self):
        self.assertEqual(concatenate_tuple((1.1, 2.2, 3.3)), "1.1-2.2-3.3")

    def test_concatenate_tuple_with_mixed_types(self):
        with self.assertRaises(TypeError):
            concatenate_tuple((1, "str", 3))
