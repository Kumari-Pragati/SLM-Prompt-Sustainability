import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):
    def test_empty_list_positive(self):
        self.assertIsInstance(empty_list(3), list)
        self.assertEqual(len(empty_list(3)), 3)
        for item in empty_list(3):
            self.assertIsInstance(item, dict)

    def test_empty_list_zero(self):
        self.assertIsInstance(empty_list(0), list)
        self.assertEqual(len(empty_list(0)), 0)

    def test_empty_list_negative(self):
        with self.assertRaises(ValueError):
            empty_list(-1)
