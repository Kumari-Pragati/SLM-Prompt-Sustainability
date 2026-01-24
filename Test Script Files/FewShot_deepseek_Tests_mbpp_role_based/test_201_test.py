import unittest
from mbpp_201_code import chkList

class TestChkList(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(chkList([1, 1, 1]))

    def test_edge_case(self):
        self.assertTrue(chkList([1]))
        self.assertFalse(chkList([]))

    def test_boundary_conditions(self):
        self.assertTrue(chkList([1, 1, 1, 1, 1]))
        self.assertFalse(chkList([1, 2, 3]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            chkList(123)
        with self.assertRaises(TypeError):
            chkList('123')
