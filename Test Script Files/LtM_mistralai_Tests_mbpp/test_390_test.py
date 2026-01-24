import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(add_string([1, 2, 3], "{}"), ["1", "2", "3"])
        self.assertEqual(add_string(["a", "b", "c"], "{}"), ["a", "b", "c"])
        self.assertEqual(add_string(["A", "B", "C"], "{}"), ["A", "B", "C"])

    def test_edge_and_boundary(self):
        self.assertEqual(add_string([], "{}"), [])
        self.assertEqual(add_string([0], "{}"), ["0"])
        self.assertEqual(add_string([1, 2, 3, 4], "{}"), ["1", "2", "3", "4"])
        self.assertEqual(add_string([-1, -2, -3], "{}"), ["-1", "-2", "-3"])
        self.assertEqual(add_string(["a", "b", "c", "d"], "{}"), ["a", "b", "c", "d"])
        self.assertEqual(add_string(["A", "B", "C", "D"], "{}"), ["A", "B", "C", "D"])
        self.assertEqual(add_string(["1", "2", "3", "4"], "{}"), ["1", "2", "3", "4"])
        self.assertEqual(add_string(["-1", "-2", "-3", "-4"], "{}"), ["-1", "-2", "-3", "-4"])

    def test_complex(self):
        self.assertEqual(add_string([1, 2, 3, 4], "{} {}{}"), ["1", "2", "34"])
        self.assertEqual(add_string(["a", "b", "c", "d"], "{} {}"), ["a", "b", "c", "d"])
        self.assertEqual(add_string(["A", "B", "C", "D"], "{} {}"), ["A", "B", "C", "D"])
        self.assertEqual(add_string(["1", "2", "3", "4"], "{} {} {}"), ["1", "2", "34"])
        self.assertEqual(add_string(["-1", "-2", "-3", "-4"], "{} {} {}"), ["-1", "-2", "-34"])
