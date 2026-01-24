import unittest
from mbpp_333_code import Sort

class TestSortFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Sort([(1, 2), (3, 4), (5, 1)]), [(5, 1), (1, 2), (3, 4)])

    def test_empty_list(self):
        self.assertEqual(Sort([]), [])

    def test_single_element(self):
        self.assertEqual(Sort([(1, 2)]), [(1, 2)])

    def test_same_second_elements(self):
        self.assertEqual(Sort([(1, 2), (3, 2)]), [(1, 2), (3, 2)])

    def test_negative_second_elements(self):
        self.assertEqual(Sort([(1, -2), (3, -4), (5, -1)]), [(5, -1), (1, -2), (3, -4)])

    def test_non_tuple_elements(self):
        with self.assertRaises(TypeError):
            Sort([1, 2, 3])

    def test_non_comparable_second_elements(self):
        with self.assertRaises(TypeError):
            Sort([(1, 'a'), (3, 'b'), (5, 'c')])
