import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):

    def test_empty_list_returns_list(self):
        result = empty_list(0)
        self.assertIsInstance(result, list)

    def test_empty_list_returns_empty_list(self):
        result = empty_list(0)
        self.assertListEqual(result, [])

    def test_empty_list_returns_list_of_dictionaries(self):
        result = empty_list(3)
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, dict)

    def test_empty_list_with_positive_integer(self):
        result = empty_list(5)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)

    def test_empty_list_with_zero(self):
        result = empty_list(0)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)
