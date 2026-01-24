import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), ((-3, -3, -3),))

    def test_edge_case_equal(self):
        self.assertEqual(substract_elements((1, 1, 1), (1, 1, 1)), ((0, 0, 0),))

    def test_edge_case_empty(self):
        self.assertEqual(substract_elements((), (1, 2, 3)), ())
        self.assertEqual(substract_elements((1, 2, 3), ()), ())

    def test_edge_case_single_element(self):
        self.assertEqual(substract_elements((1,), (2,)), ((-1,),))
        self.assertEqual(substract_elements((1,), ()), ((1,),))

    def test_edge_case_zero(self):
        self.assertEqual(substract_elements((0, 0, 0), (0, 0, 0)), ((0, 0, 0),))

    def test_error_case_mismatched_lengths(self):
        with self.assertRaises(IndexError):
            substract_elements((1, 2), (1, 2, 3))
