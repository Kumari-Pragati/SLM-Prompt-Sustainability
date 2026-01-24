import unittest
from mbpp_798_code import _sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add a list of integers
        """
        data = [1, 2, 3, 4, 5]
        result = _sum(data)
        self.assertEqual(result, 15)

    def test_list_float(self):
        """
        Test case to add a list of floats
        """
        data = [1.5, 2.5, 3.5]
        result = _sum(data)
        self.assertEqual(result, 7.5)

    def test_empty_list(self):
        """
        Test case for an empty list
        """
        data = []
        result = _sum(data)
        self.assertEqual(result, 0)

    def test_single_element(self):
        """
        Test case for a list with a single element
        """
        data = [10]
        result = _sum(data)
        self.assertEqual(result, 10)
