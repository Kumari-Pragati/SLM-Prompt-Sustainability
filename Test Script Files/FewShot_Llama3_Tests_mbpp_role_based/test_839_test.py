import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(sort_tuple(()), [])

    def test_single_element_tuple(self):
        self.assertEqual(sort_tuple([(1,)]), [(1,)])

    def test_multiple_elements_tuple(self):
        self.assertEqual(sort_tuple([(1, 2), (3, 4), (5, 6)]), [(1, 2), (3, 4), (5, 6)])

    def test_sort_by_first_element(self):
        self.assertEqual(sort_tuple([(5, 2), (1, 3), (2, 4)]), [(1, 3), (2, 4), (5, 2)])

    def test_sort_by_first_element_descending(self):
        self.assertEqual(sort_tuple([(5, 2), (1, 3), (2, 4)], descending=True), [(5, 2), (2, 4), (1, 3)])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            sort_tuple("invalid input")
