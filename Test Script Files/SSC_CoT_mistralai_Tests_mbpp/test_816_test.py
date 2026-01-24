import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(clear_tuple((1, 2, 3)), ())
        self.assertEqual(clear_tuple((0,)), ())
        self.assertEqual(clear_tuple((0, 0, 0)), ())

    def test_edge_cases(self):
        self.assertEqual(clear_tuple(()), ())
        self.assertEqual(clear_tuple((None,)), ())
        self.assertEqual(clear_tuple((True, False)), ())
        self.assertEqual(clear_tuple((1.0, 2.0, 3.0)), ())
        self.assertEqual(clear_tuple((str(1), str(2), str(3))), ())

    def test_boundary_cases(self):
        self.assertEqual(clear_tuple((-1,)), ())
        self.assertEqual(clear_tuple((1, -1)), (1,))
        self.assertEqual(clear_tuple((1, 2, -1)), (1, 2))
        self.assertEqual(clear_tuple((-1, -1, -1)), ())

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            clear_tuple(123)
        with self.assertRaises(TypeError):
            clear_tuple('abc')
        with self.assertRaises(TypeError):
            clear_tuple([1, 2, 3])
