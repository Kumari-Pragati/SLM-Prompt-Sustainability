import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):

    def test_concatenate_nested(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (4, 5, 6)
        result = concatenate_nested(test_tup1, test_tup2)
        self.assertEqual(result, (1, 2, 3, 4, 5, 6))

    def test_concatenate_nested_empty(self):
        test_tup1 = ()
        test_tup2 = ()
        result = concatenate_nested(test_tup1, test_tup2)
        self.assertEqual(result, ())

    def test_concatenate_nested_single(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = ()
        result = concatenate_nested(test_tup1, test_tup2)
        self.assertEqual(result, (1, 2, 3))

    def test_concatenate_nested_multiple(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (4, 5, 6)
        test_tup3 = (7, 8, 9)
        result = concatenate_nested(test_tup1, test_tup2, test_tup3)
        self.assertEqual(result, (1, 2, 3, 4, 5, 6, 7, 8, 9))
