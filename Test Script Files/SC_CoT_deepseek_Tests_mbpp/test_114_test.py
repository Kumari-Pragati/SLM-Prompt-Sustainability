import unittest
from mbpp_114_code import assign_freq

class TestAssignFreq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(assign_freq([1, 2, 2, 3, 3, 3]), '[([1], 1), ([2], 2), ([3], 3)]')

    def test_empty_list(self):
        self.assertEqual(assign_freq([]), '[]')

    def test_single_element(self):
        self.assertEqual(assign_freq([1]), '[([1], 1)]')

    def test_repeated_elements(self):
        self.assertEqual(assign_freq([1, 1, 1, 2, 2, 3]), '[([1], 3), ([2], 2), ([3], 1)]')

    def test_negative_numbers(self):
        self.assertEqual(assign_freq([-1, -1, 2, 2, 3, 3]), '[([-1], 2), ([2], 2), ([3], 2)]')

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            assign_freq([1, 'a', 2, 'b', 3, 'c'])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            assign_freq('1234')
