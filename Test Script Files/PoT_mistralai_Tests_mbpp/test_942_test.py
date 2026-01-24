import unittest
from mbpp_942_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_element((1, 2, 3), [1, 2, 3]))
        self.assertTrue(check_element(('a', 'b', 'c'), ['a', 'b', 'c']))
        self.assertTrue(check_element((True, False, None), [True, False]))

    def test_edge_case_empty_list(self):
        self.assertFalse(check_element((1, 2, 3), []))

    def test_edge_case_empty_tuple(self):
        self.assertFalse(check_element((), [1, 2, 3]))

    def test_edge_case_single_element(self):
        self.assertTrue(check_element((1,), [1]))
        self.assertFalse(check_element((1,), []))

    def test_edge_case_single_element_list(self):
        self.assertTrue(check_element([1], [1]))
        self.assertFalse(check_element([1], []))

    def test_edge_case_non_matching_element(self):
        self.assertFalse(check_element((1, 2, 3), [4, 5, 6]))

    def test_corner_case_none_type(self):
        self.assertRaises(TypeError, check_element, (None,), [1, 2, 3])
