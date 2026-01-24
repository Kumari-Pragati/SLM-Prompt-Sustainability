import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (4, 5, 6)
        self.assertEqual(index_multiplication(test_tup1, test_tup2), ((4,), (10,), (18,)))

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        self.assertEqual(index_multiplication(test_tup1, test_tup2), ())

    def test_single_element_tuples(self):
        test_tup1 = (1,)
        test_tup2 = (2,)
        self.assertEqual(index_multiplication(test_tup1, test_tup2), ((2,),))

    def test_tuples_of_different_lengths(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (4, 5)
        with self.assertRaises(IndexError):
            index_multiplication(test_tup1, test_tup2)
