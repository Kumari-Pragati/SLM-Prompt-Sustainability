import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):

    def test_max_val(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_val([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(max_val([1, 2, 'a', 4, 5]), 5)
        self.assertEqual(max_val([1, 2, 3, 'a', 5]), 5)
        self.assertEqual(max_val([1, 2, 3, 4, 5.5]), 5)
        self.assertEqual(max_val([1, 2, 3, 4, 'five']), 4)
        self.assertEqual(max_val([1, 2, 3, 4, 'five', 5]), 5)

    def test_max_val_empty_list(self):
        self.assertIsNone(max_val([]))

    def test_max_val_list_of_strings(self):
        self.assertIsNone(max_val(['a', 'b', 'c']))

    def test_max_val_list_of_mixed_types(self):
        self.assertEqual(max_val([1, 'a', 2, 'b', 3]), 3)
