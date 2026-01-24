import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_max([]), None)

    def test_single_element_list(self):
        self.assertEqual(find_max([['1']]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(find_max([['1', '2'], ['3', '4'], ['5', '6']]), 6)

    def test_mixed_types_list(self):
        self.assertEqual(find_max([1, '2', ['3'], 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(find_max([['-1', '-2'], ['3', '-4'], ['5', '-6']]), -6)

    def test_floats(self):
        self.assertEqual(find_max([['3.14'], ['2'], ['1.5']]), 3.14)

    def test_invalid_input(self):
        self.assertRaises(TypeError, find_max, [1, 2, '3'])
