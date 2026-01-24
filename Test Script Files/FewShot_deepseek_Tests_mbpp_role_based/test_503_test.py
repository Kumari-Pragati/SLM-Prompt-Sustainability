import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5]), [2, 3, 4, 5])

    def test_edge_condition(self):
        self.assertEqual(add_consecutive_nums([1]), [])

    def test_boundary_condition(self):
        self.assertEqual(add_consecutive_nums([1, 2]), [3])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add_consecutive_nums("1, 2, 3")

        with self.assertRaises(TypeError):
            add_consecutive_nums(1)

        with self.assertRaises(TypeError):
            add_consecutive_nums([1, "2", 3])
