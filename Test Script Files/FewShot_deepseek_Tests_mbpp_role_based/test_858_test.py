import unittest
from mbpp_858_code import count_list

class TestCountList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_list([1, 2, 3, 4, 5]), 25)

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([1]), 1)

    def test_large_list(self):
        self.assertEqual(count_list(list(range(1, 1001))), 1000000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_list("not a list")
