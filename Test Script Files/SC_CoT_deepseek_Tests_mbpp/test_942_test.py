import unittest
from mbpp_942_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_element(('a', 'b', 'c'), ['a', 'd', 'e']))

    def test_edge_case(self):
        self.assertFalse(check_element((), ['a', 'd', 'e']))
        self.assertFalse(check_element(('a', 'b', 'c'), []))

    def test_corner_case(self):
        self.assertTrue(check_element(('a', 'b', 'c'), ['a', 'a', 'a']))
        self.assertFalse(check_element(('a', 'b', 'c'), ['d', 'e', 'f']))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_element(123, ['a', 'd', 'e'])
        with self.assertRaises(TypeError):
            check_element(('a', 'b', 'c'), 'abc')
