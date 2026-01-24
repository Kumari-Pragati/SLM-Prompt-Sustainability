import unittest
from mbpp_792_code import count_list

class TestCountList(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(count_list([1, 2, 3]), 3)

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element(self):
        self.assertEqual(count_list([4]), 1)

    def test_negative_numbers(self):
        self.assertEqual(count_list([1, -2, 3, -4]), 4)

    def test_floats(self):
        self.assertEqual(count_list([1.0, 2.0, 3.0]), 3)

    def test_strings(self):
        with self.assertRaises(TypeError):
            count_list(["a", "b", "c"])

    def test_lists_of_lists(self):
        self.assertEqual(count_list([[1], [2], [3]]), 3)

    def test_none(self):
        with self.assertRaises(TypeError):
            count_list(None)
