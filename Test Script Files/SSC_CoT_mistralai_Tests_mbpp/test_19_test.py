import unittest
from mbpp_19_code import test_duplicate

class TestDuplicate(unittest.TestCase):

    def test_normal(self):
        self.assertTrue(test_duplicate([1, 2, 2, 3]))
        self.assertTrue(test_duplicate([1, 1, 2, 3]))
        self.assertTrue(test_duplicate([2, 2, 2, 3]))

    def test_edge_and_boundary(self):
        self.assertTrue(test_duplicate([]))
        self.assertTrue(test_duplicate([1]))
        self.assertTrue(test_duplicate([1, 1, 1]))
        self.assertTrue(test_duplicate([1, 2, 3, 3]))
        self.assertTrue(test_duplicate([1, 2, 3, 4, 4, 4]))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, test_duplicate, 1)
        self.assertRaises(TypeError, test_duplicate, "str")
