import unittest
from mbpp_673_code import convert

class TestConvertFunction(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(convert([1, 2, 3]), 123)
        self.assertEqual(convert([4, 5, 6]), 456)
        self.assertEqual(convert([7, 8, 9]), 789)

    def test_edge_cases(self):
        self.assertEqual(convert([]), 0)
        self.assertEqual(convert([0]), 0)
        self.assertEqual(convert([10]), 10)
        self.assertEqual(convert([100]), 100)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            convert("abc")
        with self.assertRaises(TypeError):
            convert([1, "2", 3])

    def test_combinations(self):
        self.assertEqual(convert([1, 2, 3, 4, 5]), 12345)
        self.assertEqual(convert([10, 20, 30, 40, 50]), 10203040)
