import unittest
from mbpp_665_code import range
from six.moves import zip_longest

from move_last import move_last

class TestMoveLast(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(move_last([1, 1, 2, 1, 3, 1]), [2, 3])
        self.assertEqual(move_last([1, 1, 1, 2, 1, 3, 1]), [2, 3])
        self.assertEqual(move_last([1, 1, 1, 1, 2, 1, 3, 1]), [2, 3])

    def test_edge_cases(self):
        self.assertEqual(move_last([1]), [])
        self.assertEqual(move_last([1, 1]), [])
        self.assertEqual(move_last([1, 1, 1]), [])
        self.assertEqual(move_last([1, 1, 1, 1]), [])
        self.assertEqual(move_last([1, 1, 1, 1, 1]), [])
        self.assertEqual(move_last([1, 1, 1, 1, 1, 1]), [])
        self.assertEqual(move_last([1, 1, 1, 1, 1, 1, 1]), [])
        self.assertEqual(move_last([1, 1, 1, 1, 1, 1, 1, 1]), [])

        self.assertEqual(move_last([1, 2]), [1])
        self.assertEqual(move_last([1, 2, 1]), [2])
        self.assertEqual(move_last([2, 1]), [2])

    def test_empty_list(self):
        self.assertEqual(move_last([]), [])

    def test_single_element_list(self):
        self.assertEqual(move_last([2]), [])
        self.assertEqual(move_last([3]), [])
        self.assertEqual(move_last([4]), [])

    def test_invalid_input(self):
        self.assertRaises(TypeError, move_last, 123)
        self.assertRaises(TypeError, move_last, (1, 2, 3))
        self.assertRaises(TypeError, move_last, {"a": 1, "b": 2})
