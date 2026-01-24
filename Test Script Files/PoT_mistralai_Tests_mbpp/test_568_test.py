import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):

    def test_empty_list_positive(self):
        self.assertEqual(empty_list(0), [])
        self.assertEqual(empty_list(1), [{}])
        self.assertEqual(empty_list(3), [{}, {}, {}])

    def test_empty_list_zero(self):
        self.assertIsInstance(empty_list(0), list)
        self.assertIsInstance(empty_list(0), list)

    def test_empty_list_negative(self):
        with self.assertRaises(ValueError):
            empty_list(-1)
