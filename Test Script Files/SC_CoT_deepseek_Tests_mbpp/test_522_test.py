import unittest
from mbpp_522_code import lbs

class TestLbs(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lbs([0, 8, 4, 12, 2, 10, 6, 14, 1, 9]), 7)

    def test_edge_case_single_element(self):
        self.assertEqual(lbs([5]), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(lbs([]), 0)

    def test_corner_case_decreasing_sequence(self):
        self.assertEqual(lbs([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 1)

    def test_corner_case_increasing_sequence(self):
        self.assertEqual(lbs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            lbs("1, 2, 3, 4, 5")

    def test_invalid_input_float(self):
        with self.assertRaises(TypeError):
            lbs([1.0, 2.0, 3.0, 4.0, 5.0])
