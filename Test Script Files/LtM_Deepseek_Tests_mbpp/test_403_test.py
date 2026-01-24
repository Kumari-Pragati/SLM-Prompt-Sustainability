import unittest
from mbpp_403_code import is_valid_URL

class TestIsValidURL(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_url(self):
        self.assertTrue(is_valid_URL("http://www.example.com"))
        self.assertTrue(is_valid_URL("https://www.example.com"))

    # Test for edge and boundary conditions
    def test_edge_cases(self):
        self.assertFalse(is_valid_URL(None))
        self.assertFalse(is_valid_URL(""))
        self.assertFalse(is_valid_URL("www.example.com"))
        self.assertFalse(is_valid_URL("http:/www.example.com"))
        self.assertFalse(is_valid_URL("http://"))

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertTrue(is_valid_URL("http://www.example.com/path?query=param"))
        self.assertTrue(is_valid_URL("https://user:password@www.example.com"))
        self.assertFalse(is_valid_URL("http://www.example.com/path@query=param"))
        self.assertFalse(is_valid_URL("http://www.example.com/path?query@param"))
