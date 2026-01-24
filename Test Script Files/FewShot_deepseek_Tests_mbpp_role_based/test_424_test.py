import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(extract_rear(([1, 2, 3], [4, 5, 6])), [3, 6])

    def test_empty_tuple(self):
        self.assertEqual(extract_rear(()), [])

    def test_single_element_tuple(self):
        self.assertEqual(extract_rear(([1],)), [1])

    def test_tuple_with_single_element_lists(self):
        self.assertEqual(extract_rear(([1, 2], [3, 4], [5, 6])), [2, 4, 6])

    def test_tuple_with_empty_lists(self):
        self.assertEqual(extract_rear(([], [], []), []))

    def test_tuple_with_different_length_lists(self):
        self.assertEqual(extract_rear(([1, 2, 3], [4, 5], [6])), [3, 5, 6])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_rear(123)
