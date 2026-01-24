import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(pos_nos([1, 2, 3, -1, 4]), [1, 2, 3, 4])
        self.assertEqual(pos_nos([-1, 0, 1, 2, -3]), [1, 2])
        self.assertEqual(pos_nos([0]), [0])
        self.assertEqual(pos_nos([]), [])

    def test_negative_numbers(self):
        self.assertEqual(pos_nos([-1, -2, -3]), [])
        self.assertEqual(pos_nos([-1, 0, -2, -3]), [])
        self.assertEqual(pos_nos([-1, -2, -3, 0]), [])
        self.assertEqual(pos_nos([-1, -2, -3, 0, 4]), [4])

    def test_mixed_numbers(self):
        self.assertEqual(pos_nos([1, -2, 3, -4, 5]), [1, 3, 5])
        self.assertEqual(pos_nos([-1, 0, 1, -2, 0, 3]), [1, 3])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            pos_nos(1.5)
        with self.assertRaises(TypeError):
            pos_nos("string")
