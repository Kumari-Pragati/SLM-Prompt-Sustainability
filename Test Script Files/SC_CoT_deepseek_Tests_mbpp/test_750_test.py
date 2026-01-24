import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):

    def test_typical_case(self):
        test_list = [1, 2, 3]
        test_tup = (4, 5)
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(add_tuple(test_list, test_tup), expected_output)

    def test_empty_tuple(self):
        test_list = [1, 2, 3]
        test_tup = ()
        expected_output = [1, 2, 3]
        self.assertEqual(add_tuple(test_list, test_tup), expected_output)

    def test_empty_list(self):
        test_list = []
        test_tup = (4, 5)
        expected_output = [4, 5]
        self.assertEqual(add_tuple(test_list, test_tup), expected_output)

    def test_empty_both(self):
        test_list = []
        test_tup = ()
        expected_output = []
        self.assertEqual(add_tuple(test_list, test_tup), expected_output)

    def test_invalid_input(self):
        test_list = [1, 2, 3]
        test_tup = 'a'
        with self.assertRaises(TypeError):
            add_tuple(test_list, test_tup)
