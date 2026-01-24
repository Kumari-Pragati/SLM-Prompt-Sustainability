import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(remove_duplicate("apple apple banana cherry apple"), "apple banana cherry")
        self.assertEqual(remove_duplicate("hello world hello"), "hello world")
        self.assertEqual(remove_duplicate("a b c a"), "a b c")

    def test_edge_cases(self):
        self.assertEqual(remove_duplicate(""), "")
        self.assertEqual(remove_duplicate(" "), "")
        self.assertEqual(remove_duplicate("a"), "a")
        self.assertEqual(remove_duplicate("a a a"), "a")
        self.assertEqual(remove_duplicate("apple\nbanana\ncherry"), "apple banana cherry")
        self.assertEqual(remove_duplicate("apple\nbanana\ncherry\napple"), "apple banana cherry")

    def test_special_cases(self):
        self.assertEqual(remove_duplicate("apple, apple, banana, cherry, apple"), "apple banana cherry")
        self.assertEqual(remove_duplicate("apple\tapple\tbanana\tcherry\tapple"), "apple banana cherry")
        self.assertEqual(remove_duplicate("Apple Apple Banana Cherry Apple"), "Apple Banana Cherry")
        self.assertEqual(remove_duplicate("Apple 123 Apple Banana Cherry Apple"), "Apple 123 Banana Cherry")
