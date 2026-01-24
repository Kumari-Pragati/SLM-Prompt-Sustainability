import unittest
from mbpp_431_code import common_element

class TestCommonElement(unittest.TestCase):
    def test_common_element_typical(self):
        self.assertTrue(common_element([1, 2, 3, 4], [4, 5, 6, 4]))
        self.assertTrue(common_element(["a", "b", "c", "d"], ["d", "e", "f", "d"]))

    def test_common_element_edge(self):
        self.assertTrue(common_element([], []))
        self.assertTrue(common_element([1], [1]))
        self.assertTrue(common_element([1, 2], [2]))
        self.assertTrue(common_element(["a", "b"], ["b", "c"]))
        self.assertTrue(common_element(["a", "b"], ["b", "a"]))

    def test_common_element_corner(self):
        self.assertFalse(common_element([1, 2], []))
        self.assertFalse(common_element([], [1, 2]))
        self.assertFalse(common_element([1], [2, 3]))
        self.assertFalse(common_element(["a", "b"], ["c", "d"]))
