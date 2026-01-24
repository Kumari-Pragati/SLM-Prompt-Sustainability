import unittest
from mbpp_621_code import increment_numerics

class TestIncrementNumerics(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(increment_numerics([], 3), [])

    def test_single_element_list(self):
        self.assertEqual(increment_numerics(["a"], 3), ["a"])
        self.assertEqual(increment_numerics(["1"], 3), ["4"])
        self.assertEqual(increment_numerics(["A"], 3), ["A"])

    def test_mixed_list(self):
        self.assertEqual(increment_numerics(["a", "1", "b", "0", "c"], 3), ["a", "4", "b", "3", "c"])
        self.assertEqual(increment_numerics(["A", "1", "B", "0", "C"], 3), ["A", "4", "B", "3", "C"])
        self.assertEqual(increment_numerics(["1a", "0b", "2c"], 3), ["4a", "3b", "5c"])

    def test_negative_numbers(self):
        self.assertEqual(increment_numerics(["-1", "-2", "-3"], 3), ["2", "0", "-1"])

    def test_large_numbers(self):
        self.assertEqual(increment_numerics(["999", "1000", "1001"], 3), ["1002", "1003", "1004"])
        self.assertEqual(increment_numerics(["1000000", "1000001", "1000002"], 3), ["1000003", "1000004", "1000005"])
