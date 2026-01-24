import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):

    def test_simple_tuples(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)
        self.assertEqual(tuple_to_int((0, 0, 0)), 0)
        self.assertEqual(tuple_to_int((9, 9, 9)), 729)

    def test_edge_cases(self):
        self.assertEqual(tuple_to_int(()), 0)
        self.assertEqual(tuple_to_int((10,)), 10)
        self.assertEqual(tuple_to_int((1, 10, 1)), 111)
        self.assertEqual(tuple_to_int((-1, 2, 3)), -123)
        self.assertEqual(tuple_to_int((1, -2, 3)), -123)

    def test_complex_cases(self):
        self.assertEqual(tuple_to_int((100, 200, 300)), 100200300)
        self.assertEqual(tuple_to_int((1000000, 2000000, 3000000)), 1234567890000)
        self.assertEqual(tuple_to_int((-100, -200, -300)), -1234567890000)
