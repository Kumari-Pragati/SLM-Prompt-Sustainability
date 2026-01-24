import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5], 5), 5)

    def test_edge_case(self):
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5], 0), 0)

    def test_edge_case2(self):
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5], 1), 1)

    def test_edge_case3(self):
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5], 10), 5)

    def test_edge_case4(self):
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5], 5), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            no_of_subsequences("hello", 5)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            no_of_subsequences([1, 2, 3, 4, 5], "hello")

    def test_empty_array(self):
        self.assertEqual(no_of_subsequences([], 5), 0)

    def test_array_with_single_element(self):
        self.assertEqual(no_of_subsequences([1], 5), 1)

    def test_array_with_no_elements_leaving_k(self):
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5], 0), 0)

    def test_array_with_no_elements_leaving_k2(self):
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5], 1), 1)

    def test_array_with_no_elements_leaving_k3(self):
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5], 2), 2)

    def test_array_with_no_elements_leaving_k4(self):
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5], 3), 3)
