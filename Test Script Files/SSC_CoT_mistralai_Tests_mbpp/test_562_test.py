import unittest
from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(Find_Max_Length([1, 2, 3, 4, 5]), 5)
        self.assertEqual(Find_Max_Length(["hello", "world", "this", "is", "a", "test"]), 5)

    def test_edge_cases(self):
        self.assertEqual(Find_Max_Length([1, 2, 3]), 3)
        self.assertEqual(Find_Max_Length(["hello", "world", "this", "is"]), 4)
        self.assertEqual(Find_Max_Length([1, 2, 3, 4]), 4)
        self.assertEqual(Find_Max_Length(["hello", "world", "this", "is", "a"]), 5)

    def test_empty_list(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_single_element(self):
        self.assertEqual(Find_Max_Length([1]), 1)
        self.assertEqual(Find_Max_Length(["hello"]), 5)

    def test_negative_numbers(self):
        self.assertEqual(Find_Max_Length([-1, -2, -3]), 3)

    def test_mixed_types(self):
        self.assertRaises(TypeError, Find_Max_Length, [1, "two", 3])
        self.assertRaises(TypeError, Find_Max_Length, ["one", 2, 3])
