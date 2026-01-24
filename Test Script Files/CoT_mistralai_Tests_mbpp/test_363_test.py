import unittest
from mbpp_363_code import add_K_element

class TestAddKElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], add_K_element([], 3))

    def test_single_element(self):
        self.assertListEqual([(3,)], add_K_element([(1,)], 3))

    def test_multiple_elements(self):
        self.assertListEqual([(3, 4), (5, 8)], add_K_element([(1, 2), (2, 6)], 3))

    def test_negative_K(self):
        self.assertListEqual([(-1,), (-2,)], add_K_element([(1,), (2,)], -1))

    def test_floating_point_K(self):
        self.assertListEqual([(3.5, 4.5), (5.5, 8.5)], add_K_element([(1.5, 2.5), (2.5, 6.5)], 3))

    def test_list_of_lists(self):
        self.assertListEqual([[(3,), (4,)], [(5,), (8,)]], add_K_element([[(1,), (2,)], [(2,), (6,)]], 3))

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            add_K_element(123, 4)

    def test_invalid_input_2(self.assertRaises(TypeError):
        add_K_element([(1,), (2,)], 'K')
