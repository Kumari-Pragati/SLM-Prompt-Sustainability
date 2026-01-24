import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(pos_nos([1, 2, 3, -1, 4]), [1, 2, 3, 4])
        self.assertEqual(pos_nos([0, 5, -2, 7]), [0, 5, 7])
        self.assertEqual(pos_nos([]), [])

    def test_empty_list(self):
        self.assertRaises(TypeError, pos_nos, [])

    def test_non_list_input(self):
        self.assertRaises(TypeError, pos_nos, "string")
        self.assertRaises(TypeError, pos_nos, 5)
