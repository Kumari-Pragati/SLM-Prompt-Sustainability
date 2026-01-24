import unittest
from mbpp_847_code import lcopy

class TestLcopy(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(lcopy([1, 2, 3]), [1, 2, 3])
        self.assertEqual(lcopy(["a", "b", "c"]), ["a", "b", "c"])
        self.assertEqual(lcopy((1, 2, 3)), (1, 2, 3))

    def test_empty_list(self):
        self.assertEqual(lcopy([]), [])

    def test_single_element(self):
        self.assertEqual(lcopy([0]), [0])
        self.assertEqual(lcopy(["x"]), ["x"])
        self.assertEqual(lcopy((1,)), (1,))

    def test_edge_cases(self):
        self.assertEqual(lcopy(range(10)), list(range(10)))
        self.assertEqual(lcopy(reversed([1, 2, 3])), list(reversed([1, 2, 3])))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, lcopy, 123)
        self.assertRaises(TypeError, lcopy, (1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
