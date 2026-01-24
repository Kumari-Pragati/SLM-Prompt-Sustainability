import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):

    def test_equal_arrays(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))

    def test_unequal_length(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2], 3, 2))

    def test_unequal_arrays(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 4], 3, 3))

    def test_empty_arrays(self):
        self.assertTrue(are_Equal([], [], 0, 0))

    def test_single_element_arrays(self):
        self.assertTrue(are_Equal([1], [1], 1, 1))
