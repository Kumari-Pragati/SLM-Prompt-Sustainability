import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):

    def test_empty_list(self):
        """Test get_ludic with an empty list"""
        result = get_ludic(0)
        self.assertEqual(result, [])

    def test_single_element(self):
        """Test get_ludic with a single element"""
        result = get_ludic(1)
        self.assertEqual(result, [1])

    def test_small_list(self):
        """Test get_ludic with a small list"""
        result = get_ludic(3)
        expected = [1, 2, 3]
        self.assertEqual(result, expected)

    def test_large_list(self):
        """Test get_ludic with a large list"""
        result = get_ludic(100)
        expected = list(range(1, 101))
        expected = [x for x in expected if x not in (x + i for i in range(1, x + 1))]
        self.assertEqual(result, expected)

    def test_negative_input(self):
        """Test get_ludic with a negative input"""
        with self.assertRaises(ValueError):
            get_ludic(-1)

    def test_zero_input(self):
        """Test get_ludic with zero input"""
        with self.assertRaises(ValueError):
            get_ludic(0)
