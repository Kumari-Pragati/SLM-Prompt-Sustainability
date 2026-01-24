import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(zip_tuples((1, 2, 3), (4, 5, 6)), [(3, 4), (2, 5), (1, 6)])

    def test_edge_case_empty_tuple(self):
        self.assertEqual(zip_tuples((), (1, 2, 3)), [])

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(zip_tuples((1,), (2, 3)), [(1, 2)])

    def test_edge_case_single_element_tuple2(self):
        self.assertEqual(zip_tuples((1, 2, 3), ()), [])

    def test_edge_case_single_element_tuple3(self):
        self.assertEqual(zip_tuples((1,), (4,)), [(1, 4)])

    def test_edge_case_single_element_tuple4(self):
        self.assertEqual(zip_tuples((1, 2, 3), (4, 5)), [(3, 5), (2, 4), (1, 5)])

    def test_edge_case_single_element_tuple5(self):
        self.assertEqual(zip_tuples((1, 2, 3, 4, 5), (6, 7)), [(5, 7), (4, 6), (3, 7), (2, 6), (1, 7)])

    def test_edge_case_single_element_tuple6(self):
        self.assertEqual(zip_tuples((1, 2, 3, 4, 5), (6,)), [(5, 6), (4, 6), (3, 6), (2, 6), (1, 6)])

    def test_edge_case_single_element_tuple7(self):
        self.assertEqual(zip_tuples((1, 2, 3, 4, 5), (6, 7, 8)), [(5, 8), (4, 7), (3, 8), (2, 7), (1, 8)])
