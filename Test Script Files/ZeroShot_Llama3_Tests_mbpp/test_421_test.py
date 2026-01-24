import unittest
from mbpp_421_code import concatenate_tuple

class TestConcatenateTuple(unittest.TestCase):

    def test_concatenate_tuple(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')
        self.assertEqual(concatenate_tuple((4, 5, 6)), '4-5-6')
        self.assertEqual(concatenate_tuple((7, 8, 9)), '7-8-9')
        self.assertEqual(concatenate_tuple((10, 11, 12)), '10-11-12')
        self.assertEqual(concatenate_tuple(()), '')
        self.assertEqual(concatenate_tuple((1,)), '1')
        self.assertEqual(concatenate_tuple((1, 2)), '1-2')

    def test_concatenate_tuple_edge_cases(self):
        self.assertEqual(concatenate_tuple((-1, 2, 3)), '-1-2-3')
        self.assertEqual(concatenate_tuple((1, -2, 3)), '1--2-3')
        self.assertEqual(concatenate_tuple((1, 2, -3)), '1-2--3')
        self.assertEqual(concatenate_tuple((1, 2, 3, -4)), '1-2-3--4')
