import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(multi_list(2, 3), [[0, 0, 0], [0, 2, 3], [0, 3, 6]])
        self.assertEqual(multi_list(3, 4), [[0, 0, 0, 0], [0, 0, 3, 6], [0, 3, 9, 12], [0, 6, 12, 21]])

    def test_zero_input(self):
        self.assertEqual(multi_list(0, 0), [])

    def test_negative_input(self):
        self.assertRaises(ValueError, multi_list, -1, 2)
        self.assertRaises(ValueError, multi_list, 1, -1)

    def test_one_input(self):
        self.assertEqual(multi_list(1, 1), [[0]])
        self.assertRaises(ValueError, multi_list, 1, 0)
