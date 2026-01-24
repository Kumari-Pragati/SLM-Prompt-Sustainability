import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificnum(unittest.TestCase):
    def test_all_elements_greater_than_num(self):
        list = [5, 6, 7, 8, 9]
        num = 5
        self.assertTrue(greater_specificnum(list, num))

    def test_all_elements_less_than_num(self):
        list = [1, 2, 3, 4, 5]
        num = 6
        self.assertFalse(greater_specificnum(list, num))

    def test_mixed_elements(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        num = 5
        self.assertTrue(greater_specificnum(list, num))

    def test_empty_list(self):
        list = []
        num = 5
        self.assertFalse(greater_specificnum(list, num))

    def test_num_is_zero(self):
        list = [1, 2, 3, 4, 5]
        num = 0
        self.assertFalse(greater_specificnum(list, num))
