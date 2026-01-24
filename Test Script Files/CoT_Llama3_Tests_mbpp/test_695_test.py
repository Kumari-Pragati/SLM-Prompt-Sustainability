import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_typical(self):
        self.assertTrue(check_greater((1, 2, 3), (2, 3, 4)))

    def test_edge1(self):
        self.assertFalse(check_greater((1, 2, 3), (1, 2, 3)))

    def test_edge2(self):
        self.assertTrue(check_greater((1, 2, 3), (0, 1, 2)))

    def test_edge3(self):
        self.assertFalse(check_greater((1, 2, 3), (3, 2, 1)))

    def test_edge4(self):
        self.assertTrue(check_greater((1, 2), (0, 1)))

    def test_edge5(self):
        self.assertFalse(check_greater((1, 2), (2, 1)))

    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            check_greater('test', (1, 2, 3))

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            check_greater((1, 2, 3), 'test')

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            check_greater('test', 'test')
