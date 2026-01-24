import unittest
from mbpp_792_code import count_list

class TestCountList(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(count_list([1, 2, 3, 4, 5]), 5)
        
    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)
        
    def test_single_element_list(self):
        self.assertEqual(count_list([1]), 1)
        
    def test_large_list(self):
        self.assertEqual(count_list(list(range(1, 1001))), 1000)
        
    def test_string_list(self):
        self.assertEqual(count_list(["apple", "banana", "cherry"]), 3)
        
    def test_mixed_type_list(self):
        self.assertEqual(count_list([1, "apple", 3.14, True]), 4)
        
    def test_none_input(self):
        with self.assertRaises(TypeError):
            count_list(None)
