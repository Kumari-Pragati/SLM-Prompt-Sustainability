import unittest
from mbpp_942_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_simple_case(self):
        self.assertTrue(check_element(('a', 'b', 'c'), ['a']))

    def test_edge_case_empty_tup(self):
        self.assertFalse(check_element((), ['a']))

    def test_edge_case_empty_list(self):
        self.assertFalse(check_element(('a', 'b', 'c'), []))

    def test_edge_case_empty_both(self):
        self.assertFalse(check_element((), []))

    def test_boundary_case_single_element(self):
        self.assertTrue(check_element(('a',), ['a']))
        self.assertFalse(check_element(('a',), ['b']))

    def test_complex_case_multiple_elements(self):
        self.assertTrue(check_element(('a', 'b', 'c'), ['a', 'b']))
        self.assertFalse(check_element(('a', 'b', 'c'), ['d']))

    def test_complex_case_duplicates(self):
        self.assertTrue(check_element(('a', 'b', 'c', 'a'), ['a']))
        self.assertFalse(check_element(('a', 'b', 'c', 'a'), ['b']))
