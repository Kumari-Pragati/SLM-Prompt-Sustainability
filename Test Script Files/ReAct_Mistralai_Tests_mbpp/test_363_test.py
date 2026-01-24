import unittest
from mbpp_363_code import add_K_element

class TestAddKElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(add_K_element([], 3), [])

    def test_single_element(self):
        self.assertListEqual(add_K_element([(1, 2)], 3), [(4, 5)])

    def test_multiple_elements(self):
        self.assertListEqual(add_K_element([(1, 2), (3, 4)], 3), [(4, 5), (6, 7)])

    def test_negative_K(self):
        self.assertListEqual(add_K_element([(1, 2)], -3), [(-2, -1)])

    def test_list_with_tuples_and_ints(self):
        self.assertListEqual(add_K_element([(1, 2), 3], 3), [(4, 5), (6,)])

    def test_list_with_empty_tuple(self):
        self.assertListEqual(add_K_element([(), (1, 2)], 3), [(3, 5)])

    def test_list_with_none(self):
        self.assertRaises(TypeError, add_K_element, [None, (1, 2)], 3)

    def test_list_with_string(self):
        self.assertRaises(TypeError, add_K_element, [('a', 'b'), (1, 2)], 3)
