import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):

    def test_typical_tuple(self):
        self.assertEqual(tuple_size(()), 24)
        self.assertEqual(tuple_size((1,)), 28)
        self.assertEqual(tuple_size((1, 2)), 32)
        self.assertEqual(tuple_size((1, 2, 3)), 40)

    def test_edge_cases(self):
        self.assertEqual(tuple_size((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)), 56)
        self.assertEqual(tuple_size((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)), 72)

    def test_empty_tuple(self):
        self.assertEqual(tuple_size(()), 24)

    def test_single_element_tuple(self):
        self.assertEqual(tuple_size((1,)), 28)

    def test_tuple_with_multiple_elements(self):
        self.assertEqual(tuple_size((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)), 56)

    def test_tuple_with_large_number_of_elements(self):
        self.assertEqual(tuple_size((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)), 72)

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            tuple_size("")
