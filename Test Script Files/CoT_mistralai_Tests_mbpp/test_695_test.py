import unittest
from mbpp_695_code import range
from six.moves import zip

class TestCheckGreater(unittest.TestCase):

    def test_typical_case(self):
        self.assertFalse(check_greater((1, 2, 3), (2, 3, 4)))
        self.assertFalse(check_greater((10, 20, 30), (20, 30, 40)))
        self.assertFalse(check_greater((100, 200, 300), (200, 300, 400)))

    def test_edge_case_same_elements(self):
        self.assertTrue(check_greater((1, 1, 1), (1, 1, 1)))

    def test_edge_case_one_smaller(self):
        for i in range(10):
            self.assertTrue(check_greater((i, i+1, i+2), (i+1, i+2, i+3)))

    def test_edge_case_one_larger(self):
        for i in range(10):
            self.assertFalse(check_greater((i+1, i, i-1), (i, i+1, i+2)))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, check_greater, (1, 2, 3), 'abc')
        self.assertRaises(TypeError, check_greater, [1, 2, 3], (1, 2, 3))
        self.assertRaises(TypeError, check_greater, (1, 2, 3), (1, 2))
