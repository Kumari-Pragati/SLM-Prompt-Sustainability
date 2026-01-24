import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(and_tuples((1, 2, 3), (4, 5, 6)), (0, 3, 6))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(and_tuples((), (1, 2, 3)), ())

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(and_tuples((1,), (2,)), (0,))

    def test_edge_case_single_element_tuple2(self):
        self.assertEqual(and_tuples((1, 2, 3), ()), ())

    def test_edge_case_single_element_tuple3(self):
        self.assertEqual(and_tuples((1,), (1,)), (1,))

    def test_edge_case_single_element_tuple4(self):
        self.assertEqual(and_tuples((1, 2, 3), (1,)), (0, 2, 2))

    def test_edge_case_single_element_tuple5(self):
        self.assertEqual(and_tuples((1, 2, 3), (2,)), (0, 0, 2))

    def test_edge_case_single_element_tuple6(self):
        self.assertEqual(and_tuples((1, 2, 3), (3,)), (0, 0, 0))

    def test_edge_case_single_element_tuple7(self):
        self.assertEqual(and_tuples((1, 2, 3), (4,)), (0, 0, 0))

    def test_edge_case_single_element_tuple8(self):
        self.assertEqual(and_tuples((1, 2, 3), (5,)), (0, 0, 0))

    def test_edge_case_single_element_tuple9(self):
        self.assertEqual(and_tuples((1, 2, 3), (6,)), (0, 0, 0))

    def test_edge_case_single_element_tuple10(self):
        self.assertEqual(and_tuples((1, 2, 3), (7,)), (0, 0, 0))

    def test_edge_case_single_element_tuple11(self):
        self.assertEqual(and_tuples((1, 2, 3), (8,)), (0, 0, 0))

    def test_edge_case_single_element_tuple12(self):
        self.assertEqual(and_tuples((1, 2, 3), (9,)), (0, 0, 0))

    def test_edge_case_single_element_tuple13(self):
        self.assertEqual(and_tuples((1, 2, 3), (10,)), (0, 0, 0))

    def test_edge_case_single_element_tuple14(self):
        self.assertEqual(and_tuples((1, 2, 3), (11,)), (0, 0, 0))

    def test_edge_case_single_element_tuple15(self):
        self.assertEqual(and_tuples((1, 2, 3), (12,)), (0, 0, 0))

    def test_edge_case_single_element_tuple16(self):
        self.assertEqual(and_tuples((1, 2, 3), (13,)), (0, 0, 0))

    def test_edge_case_single_element_tuple17(self):
        self.assertEqual(and_tuples((1, 2, 3), (14,)), (0, 0, 0))

    def test_edge_case_single_element_tuple18(self):
        self.assertEqual(and_tuples((1, 2, 3), (15,)), (0, 0, 0))

    def test_edge_case_single_element_tuple19(self):
        self.assertEqual(and_tuples((1, 2, 3), (16,)), (0, 0, 0))

    def test_edge_case_single_element_tuple20(self):
        self.assertEqual(and_tuples((1, 2, 3), (17,)), (0, 0, 0))

    def test_edge_case_single_element_tuple21(self):
        self.assertEqual(and_tuples((1, 2, 3), (18,)), (0, 0, 0))

    def test_edge_case_single_element_tuple22(self):
        self.assertEqual(and_tuples((1, 2, 3), (19,)), (0, 0, 0))

    def test_edge_case_single_element_tuple23(self):
        self.assertEqual(and_tuples((1, 2, 3), (20,)), (0, 0, 0))

    def test_edge_case_single_element_tuple24(self):
        self.assertEqual(and_tuples((1, 2, 3), (21,)), (0, 0, 0))

    def test_edge_case_single_element_tuple25(self):
        self.assertEqual(and_tuples((1, 2, 3), (22,)), (0, 0, 0))

    def test_edge_case_single_element_tuple26(self):
        self.assertEqual(and_tuples((1,