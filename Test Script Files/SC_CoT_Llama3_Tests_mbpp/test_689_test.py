import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):
    def test_typical_input(self):
        arr = [2, 3, 1, 1, 4]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), 2)

    def test_edge_case_zero_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), float('inf'))

    def test_edge_case_zero_first_element(self):
        arr = [0, 2, 3, 1, 1, 4]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), 1)

    def test_edge_case_last_element_reachable(self):
        arr = [1, 2, 3, 1, 1, 4]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), 3)

    def test_edge_case_last_element_unreachable(self):
        arr = [1, 2, 3, 1, 1, 0]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), float('inf'))

    def test_edge_case_all_elements_zero(self):
        arr = [0, 0, 0, 0, 0]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), float('inf'))

    def test_invalid_input_non_integer_array(self):
        arr = ['a', 2, 3, 1, 1, 4]
        n = len(arr)
        with self.assertRaises(TypeError):
            min_jumps(arr, n)

    def test_invalid_input_non_integer_n(self):
        arr = [2, 3, 1, 1, 4]
        n = 'a'
        with self.assertRaises(TypeError):
            min_jumps(arr, n)
