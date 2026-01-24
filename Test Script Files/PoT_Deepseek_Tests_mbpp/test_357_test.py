import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)

    def test_single_element(self):
        self.assertEqual(find_max([[5]]), 5)

    def test_empty_list(self):
        self.assertIsNone(find_max([]))

    def test_negative_numbers(self):
        self.assertEqual(find_max([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(find_max([[1, -2, 3], [-4, 5, -6], [7, -8, 9]]), 9)

    def test_zero(self):
        self.assertEqual(find_max([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            find_max([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])

    def test_non_list_elements(self):
        with self.assertRaises(TypeError):
            find_max(['1', '2', '3', '4', '5'])
