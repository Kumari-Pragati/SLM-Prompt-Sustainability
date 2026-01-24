import unittest
from mbpp_431_code import common_element

class TestCommonElement(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(common_element([1, 2, 3], [3, 2, 1]))
        self.assertTrue(common_element([4, 4, 4], [4, 4, 4, 4]))
        self.assertTrue(common_element(['a', 'b', 'c'], ['c', 'b', 'a']))

    def test_edge_cases(self):
        self.assertFalse(common_element([], []))
        self.assertFalse(common_element([1], []))
        self.assertFalse(common_element([], [1]))
        self.assertFalse(common_element([1], [2]))
        self.assertFalse(common_element([1, 2], []))
        self.assertTrue(common_element([1, 1], [1, 2]))
        self.assertTrue(common_element([1, 2, 3], [3, 4, 5]))
        self.assertTrue(common_element([1, 2, 3], [3, 2, 4]))
        self.assertTrue(common_element([1, 2, 3], [3, '2', 4]))
        self.assertTrue(common_element([1, 2, 3], [3, '2', '4']))
