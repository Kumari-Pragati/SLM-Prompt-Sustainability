import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):

    def test_catalan_number_zero(self):
        """Test catalan_number(0) returns 1"""
        self.assertEqual(catalan_number(0), 1)

    def test_catalan_number_one(self):
        """Test catalan_number(1) returns 1"""
        self.assertEqual(catalan_number(1), 1)

    def test_catalan_number_small_positive_integer(self):
        """Test catalan_number(2), catalan_number(3), and catalan_number(4)"""
        self.assertEqual(catalan_number(2), 2)
        self.assertEqual(catalan_number(3), 5)
        self.assertEqual(catalan_number(4), 14)

    def test_catalan_number_large_positive_integer(self):
        """Test catalan_number(10) and catalan_number(20)"""
        self.assertEqual(catalan_number(10), 19056)
        self.assertEqual(catalan_number(20), 4298172870)

    def test_catalan_number_negative_integer(self):
        """Test catalan_number(-1) raises ValueError"""
        with self.assertRaises(ValueError):
            catalan_number(-1)
