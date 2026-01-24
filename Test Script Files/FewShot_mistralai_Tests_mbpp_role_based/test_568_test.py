import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):
    def test_positive_length(self):
        self.assertEqual(empty_list(3), [{}, {}, {}])

    def test_zero_length(self):
        self.assertEqual(empty_list(0), [])

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            empty_list(-1)
