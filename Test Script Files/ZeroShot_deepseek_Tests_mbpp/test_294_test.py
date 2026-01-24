import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):

    def test_max_val_with_integers(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_val([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_val([100, 200, 300, 400, 500]), 500)

    def test_max_val_with_mixed_types(self):
        self.assertEqual(max_val([1, 2, '3', 4, 5]), 5)
        self.assertEqual(max_val([-1, -2, -3, -4, '5']), -1)
        self.assertEqual(max_val([100, 200, '300', 400, 500]), 500)

    def test_max_val_with_non_integers(self):
        self.assertIsNone(max_val(['a', 'b', 'c', 'd', 'e']))
        self.assertIsNone(max_val([]))
