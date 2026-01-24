import unittest
from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):
    def test_add_nested_tuples(self):
        self.assertEqual(add_nested_tuples((1, 2), (3, 4)), ((4, 6),))
        self.assertEqual(add_nested_tuples((1, 2, 3), (4, 5, 6)), ((5, 7, 9),))
        self.assertEqual(add_nested_tuples((1, 2, 3, 4), (5, 6, 7, 8)), ((6, 8, 10, 12),))
        self.assertEqual(add_nested_tuples((1, 2), ()), ((1,),))
        self.assertEqual(add_nested_tuples((), (1, 2)), ((1, 2),))
        self.assertEqual(add_nested_tuples((1, 2, 3), (4, 5)), ((5, 7),))
        self.assertEqual(add_nested_tuples((1, 2, 3, 4), (5, 6)), ((6, 8, 10),))
        self.assertEqual(add_nested_tuples((1, 2, 3, 4, 5), (6, 7, 8, 9, 10)), ((7, 9, 11, 13, 15),))
        self.assertEqual(add_nested_tuples((1, 2, 3, 4, 5, 6), (7, 8, 9, 10, 11, 12),), ((8, 10, 12, 14, 16, 18),))
