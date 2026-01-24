import unittest
from mbpp_819_code import count_duplic

class TestCountDuplic(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_duplic([1,1,2,2,3,3,3]), ([1,2,3], [2,2,3]))

    def test_single_element(self):
        self.assertEqual(count_duplic([1]), ([1], [1]))

    def test_empty_list(self):
        self.assertEqual(count_duplic([]), ([], []))

    def test_edge_case(self):
        self.assertEqual(count_duplic([1,1]), ([1], [2]))

    def test_corner_case(self):
        self.assertEqual(count_duplic([1,2,2,1]), ([1,2], [1,2]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_duplic('1234')
