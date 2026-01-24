import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(average_tuple([(1, 2, 3), (4, 5, 6), (7, 8, 9)]), [(5.0, 5.0, 5.0)])

    def test_edge_case_empty_input(self):
        self.assertListEqual(average_tuple([]), [])

    def test_edge_case_single_input(self):
        self.assertListEqual(average_tuple([(1)]), [1.0])

    def test_edge_case_single_element_input(self):
        self.assertListEqual(average_tuple([(1,)]), [1.0])

    def test_edge_case_negative_numbers(self):
        self.assertListEqual(average_tuple([(-1, 2, -3), (4, -5, 6), (-7, 8, -9)]), [(-1.0, -1.0, -1.0)])

    def test_corner_case_mixed_types(self):
        self.assertRaises(TypeError, average_tuple, [(1, 'a'), (2, 'b')])
