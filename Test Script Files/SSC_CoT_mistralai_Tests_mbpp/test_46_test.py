import unittest
from mbpp_46_code import test_distinct

class TestDistinct(unittest.TestCase):
    def test_normal(self):
        self.assertTrue(test_distinct([1, 2, 3, 4, 5]))
        self.assertTrue(test_distinct([10, 20, 30, 40, 50]))
        self.assertTrue(test_distinct(["a", "b", "c", "d", "e"]))

    def test_edge_cases(self):
        self.assertTrue(test_distinct([1, 1, 2, 3, 4, 5]))
        self.assertTrue(test_distinct([1, 2, 3, 4, 5, 5]))
        self.assertTrue(test_distinct(["a", "b", "b", "c", "d", "e"]))
        self.assertTrue(test_distinct([1, 2, 3, 4, 5, 5.0]))
        self.assertTrue(test_distinct([1j, 2j, 3j, 4j, 5j]))

    def test_empty_list(self):
        self.assertTrue(test_distinct([]))

    def test_single_element(self):
        self.assertTrue(test_distinct([1]))
        self.assertTrue(test_distinct([1.0]))
        self.assertTrue(test_distinct([1j]))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, test_distinct, (1, 2, 3))
        self.assertRaises(TypeError, test_distinct, {1: 2, 3: 4})
        self.assertRaises(TypeError, test_distinct, [1, 2, 3.0])
        self.assertRaises(TypeError, test_distinct, [1, 2j, 3])
