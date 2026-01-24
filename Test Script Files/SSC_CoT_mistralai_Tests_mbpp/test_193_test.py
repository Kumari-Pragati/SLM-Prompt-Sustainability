import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(remove_tuple((1, 2, 3, 1, 2)), (1, 2, 3))

    def test_edge_input(self):
        self.assertEqual(remove_tuple((0, 1, 2)), (1, 2))
        self.assertEqual(remove_tuple((1, 0, 2)), (1, 2))
        self.assertEqual(remove_tuple((1, 2, 0)), (1, 2))

    def test_boundary_input(self):
        self.assertEqual(remove_tuple(()), ())
        self.assertEqual(remove_tuple((1,)), (1,))
        self.assertEqual(remove_tuple((1,) * 100), (1,))

    def test_special_input(self):
        self.assertEqual(remove_tuple((1, 1, 1)), (1,))
        self.assertEqual(remove_tuple((1, 1.0, 1)), (1, 1.0))
        self.assertEqual(remove_tuple((1, '1', 1)), (1, '1'))

    def test_invalid_input(self):
        self.assertRaises(TypeError, remove_tuple, 123)
        self.assertRaises(TypeError, remove_tuple, (1, 'a'))
