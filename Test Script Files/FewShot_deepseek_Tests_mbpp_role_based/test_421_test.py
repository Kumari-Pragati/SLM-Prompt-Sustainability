import unittest
from mbpp_421_code import concatenate_tuple

class TestConcatenateTuple(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(concatenate_tuple(('a', 'b', 'c')), 'a-b-c')

    def test_empty_tuple(self):
        self.assertEqual(concatenate_tuple(()), '')

    def test_single_element_tuple(self):
        self.assertEqual(concatenate_tuple(('a',)), 'a')

    def test_numeric_tuple(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')

    def test_mixed_type_tuple(self):
        self.assertEqual(concatenate_tuple(('a', 2, 'c')), 'a-2-c')

    def test_large_tuple(self):
        test_tup = tuple(str(i) for i in range(1000))
        expected_result = '-'.join(test_tup)
        self.assertEqual(concatenate_tuple(test_tup), expected_result)
