import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):

    def test_empty_list_positive(self):
        "Test empty_list with positive integer"
        result = empty_list(5)
        self.assertEqual(len(result), 5)
        for item in result:
            self.assertDictEqual(item, {})

    def test_empty_list_zero(self):
        "Test empty_list with zero"
        result = empty_list(0)
        self.assertEqual(len(result), 0)

    def test_empty_list_negative(self):
        "Test empty_list with negative integer"
        with self.assertRaises(ValueError):
            empty_list(-1)
