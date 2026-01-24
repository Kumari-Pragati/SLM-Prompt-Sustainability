import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):

    def test_max_of_two_typical(self):
        self.assertEqual(max_of_two(5, 3), 5)

    def test_max_of_two_edge(self):
        self.assertEqual(max_of_two(5, 5), 5)

    def test_max_of_two_negative(self):
        self.assertEqual(max_of_two(-5, -3), -5)

    def test_max_of_two_zero(self):
        self.assertEqual(max_of_two(0, 0), 0)

    def test_max_of_two_negative_edge(self):
        self.assertEqual(max_of_two(-5, 0), -5)

    def test_max_of_two_error(self):
        with self.assertRaises(TypeError):
            max_of_two('a', 'b')
