import unittest
from mbpp_942_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(check_element((1, 2, 3), [1, 2, 3]))
        self.assertTrue(check_element(('a', 'b', 'c'), ['a', 'b', 'c']))
        self.assertTrue(check_element((True, False, None), [True, False]))

    def test_edge_cases(self):
        self.assertFalse(check_element((1, 2, 3), []))
        self.assertFalse(check_element((1, 2, 3), [4]))
        self.assertFalse(check_element(('a', 'b', 'c'), ['z']))
        self.assertFalse(check_element((True, False, None), [True, False, 'x']))

    def test_boundary_cases(self):
        self.assertTrue(check_element((), [None]))
        self.assertTrue(check_element(('',), [' ']))
        self.assertTrue(check_element((None,), [None]))
        self.assertTrue(check_element((1.0,), [1]))

    def test_invalid_input(self):
        self.assertRaises(TypeError, check_element, (1, 2, 3), 4)
        self.assertRaises(TypeError, check_element, ('a', 'b', 'c'), 4)
        self.assertRaises(TypeError, check_element, (1, 2, 3), [4, 'x'])
