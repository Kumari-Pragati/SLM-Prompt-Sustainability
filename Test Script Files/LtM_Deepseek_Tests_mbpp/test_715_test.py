import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(str_to_tuple("1, 2, 3"), (1, 2, 3))

    def test_edge_conditions(self):
        self.assertEqual(str_to_tuple(""), ())
        self.assertEqual(str_to_tuple("0"), (0,))

    def test_boundary_conditions(self):
        self.assertEqual(str_to_tuple("2147483647, 2147483647"), (2147483647, 2147483647))
        self.assertEqual(str_to_tuple("-2147483648, -2147483648"), (-2147483648, -2147483648))

    def test_complex_cases(self):
        self.assertEqual(str_to_tuple("1, 2, 3, 4, 5"), (1, 2, 3, 4, 5))
        self.assertEqual(str_to_tuple("10, 20, 30, 40, 50"), (10, 20, 30, 40, 50))
