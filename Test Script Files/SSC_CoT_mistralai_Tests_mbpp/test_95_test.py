import unittest
from mbpp_95_code import Find_Min_Length

class TestFindMinLength(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(Find_Min_Length([1, 2, 3, 4, 5]), 1)
        self.assertEqual(Find_Min_Length(["apple", "banana", "cherry"]), 5)
        self.assertEqual(Find_Min_Length([1.0, 2.0, 3.0]), 1)

    def test_edge_cases(self):
        self.assertEqual(Find_Min_Length([0, 0, 0]), 1)
        self.assertEqual(Find_Min_Length([1, 0, 3]), 1)
        self.assertEqual(Find_Min_Length(["a", "", "b"]), 1)

    def test_empty_list(self):
        self.assertEqual(Find_Min_Length([]), 0)

    def test_single_item(self):
        self.assertEqual(Find_Min_Length([1]), 1)
        self.assertEqual(Find_Min_Length(["a"]), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Find_Min_Length(123)
        with self.assertRaises(TypeError):
            Find_Min_Length((1, 2, 3))
