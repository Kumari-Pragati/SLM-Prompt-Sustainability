import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup1 = (1, 2, 3, 4, 5)
        test_tup2 = (4, 5, 6, 7, 8)
        self.assertEqual(union_elements(test_tup1, test_tup2), (1, 2, 3, 4, 5, 6, 7, 8))

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        self.assertEqual(union_elements(test_tup1, test_tup2), ())

    def test_single_tuple(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = ()
        self.assertEqual(union_elements(test_tup1, test_tup2), (1, 2, 3))

    def test_duplicates(self):
        test_tup1 = (1, 2, 2, 3, 4)
        test_tup2 = (2, 3, 4, 5, 6)
        self.assertEqual(union_elements(test_tup1, test_tup2), (1, 2, 3, 4, 5, 6))
