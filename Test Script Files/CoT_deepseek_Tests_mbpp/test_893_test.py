import unittest
from mbpp_893_code import Extract

class TestExtract(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])

    def test_single_item(self):
        self.assertEqual(Extract([[1]]), [1])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_element_in_list(self):
        self.assertEqual(Extract([[1, 2]]), [2])

    def test_empty_sublists(self):
        self.assertEqual(Extract([[], []]), [])

    def test_negative_numbers(self):
        self.assertEqual(Extract([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), [-3, -6, -9])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            Extract([[1, 'a'], [2, 'b'], [3, 'c']])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            Extract(123)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            Extract(None)
