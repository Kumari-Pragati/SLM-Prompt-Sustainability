import unittest
from mbpp_587_code import list_tuple

class TestListTuple(unittest.TestCase):
    def test_normal_input(self):
        self.assertIsInstance(list_tuple([1, 2, 3]), tuple)
        self.assertEqual(list_tuple([1, 2, 3]), (1, 2, 3))

    def test_empty_list(self):
        self.assertIsInstance(list_tuple([]), tuple)
        self.assertEqual(list_tuple([]), ())

    def test_single_element_list(self):
        self.assertIsInstance(list_tuple([4]), tuple)
        self.assertEqual(list_tuple([4]), (4,))

    def test_negative_numbers(self):
        self.assertIsInstance(list_tuple([-1, -2, -3]), tuple)
        self.assertEqual(list_tuple([-1, -2, -3]), (-1, -2, -3))

    def test_mixed_types(self):
        self.assertRaises(TypeError, list_tuple, [1, 2, "3", 4])

    def test_list_with_tuple(self):
        self.assertIsInstance(list_tuple([(1, 2), 3]), tuple)
        self.assertEqual(list_tuple([(1, 2), 3]), ((1, 2), 3))
