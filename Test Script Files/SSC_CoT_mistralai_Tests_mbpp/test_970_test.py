import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(min_of_two(1, 2), 1)
        self.assertEqual(min_of_two(2, 1), 1)

    def test_edge_case_zero(self):
        self.assertEqual(min_of_two(0, 1), 0)
        self.assertEqual(min_of_two(1, 0), 0)

    def test_edge_case_negative(self):
        self.assertEqual(min_of_two(-1, -2), -1)
        self.assertEqual(min_of_two(-2, -1), -1)

    def test_invalid_input_type(self):
        self.assertRaises(TypeError, min_of_two, 'a', 1)
        self.assertRaises(TypeError, min_of_two, 1, 'a')
