import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(tuple_str_int("1, 2, 3"), (1, 2, 3))

    def test_edge_conditions(self):
        self.assertEqual(tuple_str_int(""), ())
        self.assertEqual(tuple_str_int("1"), (1,))
        self.assertEqual(tuple_str_int("1, 2, 3, 4, 5"), (1, 2, 3, 4, 5))

    def test_boundary_conditions(self):
        self.assertEqual(tuple_str_int("0, 1, 2, 3, 4, 5, 6, 7, 8, 9"), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
        self.assertEqual(tuple_str_int("10, 20, 30, 40, 50, 60, 70, 80, 90, 100"), (10, 20, 30, 40, 50, 60, 70, 80, 90, 100))

    def test_complex_cases(self):
        self.assertEqual(tuple_str_int("1, 2, 3, 4, 5, 6, 7, 8, 9, 10"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
        self.assertEqual(tuple_str_int("10, 20, 30, 40, 50, 60, 70, 80, 90, 100"), (10, 20, 30, 40, 50, 60, 70, 80, 90, 100))
