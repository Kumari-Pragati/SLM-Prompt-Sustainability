import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(add_tuple([1, 2, 3], (4, 5)), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(add_tuple([], (1, 2, 3)), (1, 2, 3))

    def test_single_element_list(self):
        self.assertEqual(add_tuple([1], (2, 3)), [1, 2, 3])

    def test_single_element_tuple(self):
        self.assertEqual(add_tuple([1, 2, 3], (1,)), [1, 2, 3, 1])

    def test_empty_tuple(self):
        self.assertEqual(add_tuple([1, 2, 3], ()), [1, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(add_tuple([1, -2, 3], (4, -5, 6)), [1, -2, 3, 4, -5, 6])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            add_tuple([1, 2, 3], (1, 2, "3"))
