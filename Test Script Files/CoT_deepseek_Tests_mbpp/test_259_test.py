import unittest
from mbpp_259_code import maximize_elements

class TestMaximizeElements(unittest.TestCase):

    def test_typical_case(self):
        test_tup1 = ((1, 2, 3), (4, 5, 6))
        test_tup2 = ((7, 8, 9), (10, 11, 12))
        expected_output = ((7, 8, 9), (10, 11, 12))
        self.assertEqual(maximize_elements(test_tup1, test_tup2), expected_output)

    def test_edge_case(self):
        test_tup1 = ((1, 2, 3), (4, 5, 6))
        test_tup2 = ((7, 8, 9), (10, 11, 12))
        expected_output = ((7, 8, 9), (10, 11, 12))
        self.assertEqual(maximize_elements(test_tup1, test_tup2), expected_output)

    def test_invalid_input(self):
        test_tup1 = ((1, 2, 3), (4, 5, 6))
        test_tup2 = ((7, 8, 9), (10, 11, 12))
        with self.assertRaises(TypeError):
            maximize_elements(test_tup1, test_tup2, 1)
