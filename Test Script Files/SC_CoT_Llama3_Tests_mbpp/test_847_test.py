import unittest
from mbpp_847_code import lcopy

class TestLcopy(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(lcopy([1, 2, 3]), [1, 2, 3])
        self.assertEqual(lcopy("hello"), "hello")
        self.assertEqual(lcopy((1, 2, 3)), (1, 2, 3))

    def test_edge_cases(self):
        self.assertEqual(lcopy([1, 2, 3])[:], [1, 2, 3])
        self.assertEqual(lcopy("hello")[:], "hello")
        self.assertEqual(lcopy((1, 2, 3))[:], (1, 2, 3))

    def test_empty_input(self):
        self.assertEqual(lcopy([]), [])
        self.assertEqual(lcopy(()), ())
        self.assertEqual(lcopy(""), "")

    def test_single_element_input(self):
        self.assertEqual(lcopy([1]), [1])
        self.assertEqual(lcopy("a"), "a")
        self.assertEqual(lcopy((1,)), (1,))

    def test_large_input(self):
        xs = [i for i in range(1000)]
        self.assertEqual(lcopy(xs), xs)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            lcopy(None)
        with self.assertRaises(TypeError):
            lcopy(123)
