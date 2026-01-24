import unittest
from mbpp_942_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_element(('a', 'b', 'c'), ['a']))
        self.assertTrue(check_element(('a', 'b', 'c'), ['b']))
        self.assertTrue(check_element(('a', 'b', 'c'), ['c']))

    def test_edge_case(self):
        self.assertFalse(check_element(('a', 'b', 'c'), []))
        self.assertFalse(check_element((), ['a']))
        self.assertFalse(check_element((), []))

    def test_boundary_case(self):
        self.assertTrue(check_element(('a',), ['a']))
        self.assertFalse(check_element(('a',), []))

    def test_corner_case(self):
        self.assertFalse(check_element(('a', 'b', 'c'), ['d']))
        self.assertFalse(check_element(('a', 'b', 'c'), ['a', 'b', 'c']))
