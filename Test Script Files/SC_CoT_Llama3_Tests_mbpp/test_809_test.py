import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):

    def test_typical(self):
        self.assertTrue(check_smaller((1, 2, 3), (0, 1, 2)))

    def test_edge_case(self):
        self.assertFalse(check_smaller((1, 1, 1), (1, 1, 1)))

    def test_edge_case2(self):
        self.assertTrue(check_smaller((1, 2, 3), (1, 1, 2)))

    def test_edge_case3(self):
        self.assertFalse(check_smaller((1, 2, 3), (2, 3, 4)))

    def test_edge_case4(self):
        self.assertTrue(check_smaller((1, 2, 3), (1, 2, 3)))

    def test_edge_case5(self):
        self.assertFalse(check_smaller((1, 2, 3), (3, 2, 1)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_smaller('test', (1, 2, 3))

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            check_smaller((1, 2, 3), 'test')

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            check_smaller('test', 'test')
