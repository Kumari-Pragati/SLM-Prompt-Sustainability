import unittest
from mbpp_95_code import Find_Min_Length

class TestFindMinLength(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Find_Min_Length(['hello', 'world']), 5)
        self.assertEqual(Find_Min_Length(['a', 'bb', 'ccc']), 1)

    def test_edge_conditions(self):
        self.assertEqual(Find_Min_Length(['']), 0)
        self.assertEqual(Find_Min_Length(['a']), 1)

    def test_boundary_conditions(self):
        self.assertEqual(Find_Min_Length(['abcdefghijklmnopqrstuvwxyz']), 1)
        self.assertEqual(Find_Min_Length(['abcdefghijklmnopqrstuvwxyz'*10]), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Find_Min_Length(123)
        with self.assertRaises(TypeError):
            Find_Min_Length(['hello', 123])
