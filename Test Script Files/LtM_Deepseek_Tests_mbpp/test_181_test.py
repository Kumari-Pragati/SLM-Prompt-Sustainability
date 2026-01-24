import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(common_prefix(["flower", "flow", "flight"], 3), "fl")
        self.assertEqual(common_prefix(["dog", "racecar", "car"], 3), "")
        self.assertEqual(common_prefix(["hello", "hello", "hello"], 3), "hello")

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(common_prefix([""], 1), "")
        self.assertEqual(common_prefix(["a"], 1), "a")
        self.assertEqual(common_prefix([], 0), "")

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(common_prefix(["abc", "abcd", "abce"], 3), "abc")
        self.assertEqual(common_prefix(["abc", "abd", "ab"], 3), "ab")
