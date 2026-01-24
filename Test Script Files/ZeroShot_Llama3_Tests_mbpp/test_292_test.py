import unittest
from mbpp_292_code import find

class TestFindFunction(unittest.TestCase):

    def test_find_positive_numbers(self):
        self.assertEqual(find(10,2), 5)
        self.assertEqual(find(15,3), 5)
        self.assertEqual(find(20,4), 5)
        self.assertEqual(find(25,5), 5)

    def test_find_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            find(10,0)

    def test_find_negative_numbers(self):
        self.assertEqual(find(-10,2), 5)
        self.assertEqual(find(-15,3), 5)
        self.assertEqual(find(-20,4), 5)
        self.assertEqual(find(-25,5), 5)

    def test_find_non_integer_numbers(self):
        self.assertEqual(find(10.5,2), 5)
        self.assertEqual(find(-10.5,2), 5)
        self.assertEqual(find(10,2.5), 4)
        self.assertEqual(find(-10,2.5), 4)
