import unittest
from mbpp_421_code import concatenate_tuple

class TestConcatenateTuple(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = (1, 2, 3)
        self.assertEqual(concatenate_tuple(test_tup), "1-2-3")

    def test_empty_tuple(self):
        test_tup = ()
        self.assertEqual(concatenate_tuple(test_tup), "")

    def test_single_element_tuple(self):
        test_tup = (4,)
        self.assertEqual(concatenate_tuple(test_tup), "4")

    def test_multiple_delimiters(self):
        test_tup = (1, 2, 3, 4, 5)
        self.assertEqual(concatenate_tuple(test_tup), "1-2-3-4-5")

    def test_large_tuple(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(concatenate_tuple(test_tup), "1-2-3-4-5-6-7-8-9-10")
