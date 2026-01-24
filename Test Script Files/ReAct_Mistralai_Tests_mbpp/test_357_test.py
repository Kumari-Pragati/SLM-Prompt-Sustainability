import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(ValueError, find_max, [])

    def test_single_element_list(self):
        self.assertEqual(find_max(['1']), 1)

    def test_single_integer_list(self):
        self.assertEqual(find_max([1]), 1)

    def test_multiple_integer_lists(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)

    def test_negative_numbers(self):
        self.assertEqual(find_max([[-1, -2, -3], [4, -5, 6], [-7, 8, -9]]), -1)

    def test_mixed_types(self):
        self.assertRaises(TypeError, find_max, [[1, '2', 3], [4, 5, '6'], [7, 8, 9.5]])

    def test_floats(self):
        self.assertAlmostEqual(find_max([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]]), 9.9)
