import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(extract_rear(()), [])

    def test_single_element_input(self):
        self.assertEqual(extract_rear([(1,)]), [(1,)])

    def test_multiple_elements_input(self):
        self.assertEqual(extract_rear([(1, 2), (3, 4)]), [(2,), (4,)])

    def test_empty_sub_elements(self):
        self.assertEqual(extract_rear([(1, 2, 3), (), (4, 5)]), [(3,), (), (5,)])

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            extract_rear([(1, 2, 3)])

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            extract_rear([1, 2, 3])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            extract_rear({'a': 1, 'b': 2})
