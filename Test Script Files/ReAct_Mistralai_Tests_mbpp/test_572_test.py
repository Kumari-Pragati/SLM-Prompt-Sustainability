import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(two_unique_nums([]), [])

    def test_single_element_list(self):
        for num in range(10):
            self.assertListEqual(two_unique_nums([num]), [num])

    def test_duplicate_elements(self):
        for num in range(10):
            for duplicate in range(num+1, 20):
                self.assertListEqual(two_unique_nums([num, num]), [])

    def test_multiple_unique_elements(self):
        for num1 in range(10):
            for num2 in range(num1+1, 20):
                test_list = [num1, num2]
                self.assertListEqual(two_unique_nums(test_list), test_list)

    def test_list_with_only_duplicates(self):
        for num in range(10):
            self.assertListEqual(two_unique_nums([num, num]), [])

    def test_large_list(self):
        large_list = [i for i in range(100)]
        self.assertListEqual(two_unique_nums(large_list), list(set(large_list)))
