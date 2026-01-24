import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificNum(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(greater_specificnum([1, 2, 3, 4, 5], 1))
        self.assertTrue(greater_specificnum([-1, -2, -3, -4, -5], -6))

    def test_edge_cases(self):
        self.assertFalse(greater_specificnum([0, 0, 0, 0, 0], 1))
        self.assertFalse(greater_specificnum([1, 0, 3, 4, 5], 0))
        self.assertFalse(greater_specificnum([1, 2, 3, 4, 5], 6))
        self.assertFalse(greater_specificnum([-1, -2, -3, -4, -5], -7))

    def test_empty_list(self):
        self.assertIs(greater_specificnum([]), False)

    def test_single_element(self):
        self.assertIs(greater_specificnum([1]), True)
        self.assertIs(greater_specificnum([-1]), False)

    def test_non_numeric_input(self):
        self.assertRaises(TypeError, greater_specificnum, [1, 2, 3], 'a')
        self.assertRaises(TypeError, greater_specificnum, ['1', '2', '3'], 4)
