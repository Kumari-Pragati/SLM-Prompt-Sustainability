import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificNum(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(greater_specificnum([], 10))

    def test_single_element_list(self):
        self.assertFalse(greater_specificnum([1], 2))
        self.assertTrue(greater_specificnum([2], 2))

    def test_multiple_elements_list(self):
        self.assertFalse(greater_specificnum([1, 2], 3))
        self.assertTrue(greater_specificnum([3, 4], 3))
        self.assertTrue(greater_specificnum([2, 3, 4], 2))
        self.assertTrue(greater_specificnum([2, 3, 4], 4))
