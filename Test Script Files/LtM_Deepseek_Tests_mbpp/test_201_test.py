import unittest
from mbpp_201_code import chkList

class TestChkList(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(chkList([1, 1, 1]))
        self.assertTrue(chkList(['a', 'a', 'a']))
        self.assertTrue(chkList([True, True, True]))

    def test_edge_conditions(self):
        self.assertTrue(chkList([]))
        self.assertTrue(chkList([1]))
        self.assertTrue(chkList(['a']))
        self.assertTrue(chkList([True]))

    def test_boundary_conditions(self):
        self.assertTrue(chkList([1, 1]))
        self.assertTrue(chkList(['a', 'a']))
        self.assertTrue(chkList([True, True]))

    def test_complex_cases(self):
        self.assertFalse(chkList([1, 2, 3]))
        self.assertFalse(chkList(['a', 'b', 'c']))
        self.assertFalse(chkList([True, False]))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            chkList(123)
        with self.assertRaises(TypeError):
            chkList('abc')
        with self.assertRaises(TypeError):
            chkList(None)
