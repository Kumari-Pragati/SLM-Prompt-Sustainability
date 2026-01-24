import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):
    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(sum_list([-1, 0, 1], [1, 2, 3]), [0, 2, 4])
        self.assertEqual(sum_list([1, 2, 3], [4, 5, 6, 7]), [5, 7, 9])
        self.assertEqual(sum_list([1, 2, 3, 4], [4, 5, 6, 7]), [5, 7, 9, 11])
        self.assertEqual(sum_list([], []), [])
        self.assertEqual(sum_list([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(sum_list([], [1, 2, 3]), [1, 2, 3])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_list([1, 2, 3],'string')
        with self.assertRaises(TypeError):
            sum_list('string', [1, 2, 3])
        with self.assertRaises(TypeError):
            sum_list([1, 2, 3], [1, 2, 3,'string'])
        with self.assertRaises(TypeError):
            sum_list([1, 2, 3, 4], [1, 2, 3, 4,'string'])
