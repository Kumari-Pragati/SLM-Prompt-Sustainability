import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_element([1, 1, 1], 1))
        self.assertTrue(check_element(['a', 'a', 'a'], 'a'))
        self.assertTrue(check_element([3.14, 3.14, 3.14], 3.14))

    def test_edge_case(self):
        self.assertFalse(check_element([1, 1, 2], 1))
        self.assertFalse(check_element(['a', 'a', 'b'], 'a'))
        self.assertFalse(check_element([3.14, 3.14, 3.15], 3.14))

    def test_boundary_case(self):
        self.assertFalse(check_element([], 1))
        self.assertFalse(check_element([1], 1))
        self.assertFalse(check_element([1, 1], 2))
        self.assertFalse(check_element(['a'], 'a'))
        self.assertFalse(check_element(['a', 'a'], 'b'))
        self.assertFalse(check_element([3.14], 3.14))
        self.assertFalse(check_element([3.14, 3.14], 3.15))
