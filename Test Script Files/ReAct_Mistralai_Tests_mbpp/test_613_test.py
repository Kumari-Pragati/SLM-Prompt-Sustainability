import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(maximum_value([]), [])

    def test_single_element_list(self):
        self.assertEqual(maximum_value([(1, [1])]), [(1, 1)])

    def test_multiple_elements_same_value(self):
        self.assertEqual(maximum_value([(1, [1, 1]), (2, [2, 2]), (3, [3, 3])]),
                         [(1, 1), (2, 2), (3, 3)])

    def test_multiple_elements_different_values(self):
        self.assertEqual(maximum_value([(1, [1, 2]), (2, [3, 4]), (3, [5, 6])]),
                         [(2, 4), (3, 6), (1, 2)])

    def test_negative_numbers(self):
        self.assertEqual(maximum_value([(1, [-1, -2]), (2, [-3, -4]), (3, [-5, -6])]),
                         [(2, -3), (3, -5), (1, -1)])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            maximum_value([(1, [1, 2]), (2, 'three'), (3, [5, 6])])

    def test_list_with_no_values(self):
        with self.assertRaises(ValueError):
            maximum_value([(1, []), (2, [])])
