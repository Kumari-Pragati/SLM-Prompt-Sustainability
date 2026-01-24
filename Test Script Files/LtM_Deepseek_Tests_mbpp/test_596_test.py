import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):

    def test_simple_tuple(self):
        self.assertLessEqual(tuple_size(()), 56)
        self.assertLessEqual(tuple_size((1,)), 72)
        self.assertLessEqual(tuple_size((1, 2)), 88)
        self.assertLessEqual(tuple_size((1, 2, 3)), 104)

    def test_edge_conditions(self):
        self.assertEqual(tuple_size(()), 56)
        self.assertLessEqual(tuple_size((1,) * 1000), 8800)

    def test_complex_scenarios(self):
        self.assertLessEqual(tuple_size((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)), 120)
        self.assertLessEqual(tuple_size((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)), 136)
