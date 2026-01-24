import unittest
from mbpp_431_code import common_element

class TestCommonElement(unittest.TestCase):
    def test_common_element_typical(self):
        self.assertTrue(common_element([1, 2, 3], [2, 3, 4]))
        self.assertTrue(common_element(['a', 'b', 'c'], ['b', 'c', 'd']))

    def test_common_element_edge(self):
        self.assertTrue(common_element([1, 2, 3], [1, 2, 3]))
        self.assertTrue(common_element(['a', 'b', 'c'], ['a', 'b', 'c']))

    def test_common_element_empty(self):
        self.assertFalse(common_element([], [1, 2, 3]))
        self.assertFalse(common_element([1, 2, 3], []))

    def test_common_element_single_element(self):
        self.assertTrue(common_element([1], [1]))
        self.assertFalse(common_element([1], [2]))

    def test_common_element_no_common(self):
        self.assertFalse(common_element([1, 2, 3], [4, 5, 6]))
