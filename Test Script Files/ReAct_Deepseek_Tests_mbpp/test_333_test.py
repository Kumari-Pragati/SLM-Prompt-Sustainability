import unittest
from mbpp_333_code import Sort

class TestSortFunction(unittest.TestCase):

    def test_typical_case(self):
        data = [('apple', 10), ('banana', 5), ('cherry', 20)]
        expected_output = [('cherry', 20), ('apple', 10), ('banana', 5)]
        self.assertEqual(Sort(data), expected_output)

    def test_empty_list(self):
        data = []
        expected_output = []
        self.assertEqual(Sort(data), expected_output)

    def test_single_element(self):
        data = [('apple', 10)]
        expected_output = [('apple', 10)]
        self.assertEqual(Sort(data), expected_output)

    def test_duplicate_elements(self):
        data = [('apple', 10), ('banana', 5), ('banana', 15)]
        expected_output = [('banana', 15), ('apple', 10), ('banana', 5)]
        self.assertEqual(Sort(data), expected_output)

    def test_same_second_value(self):
        data = [('apple', 10), ('banana', 10), ('cherry', 20)]
        expected_output = [('cherry', 20), ('apple', 10), ('banana', 10)]
        self.assertEqual(Sort(data), expected_output)
