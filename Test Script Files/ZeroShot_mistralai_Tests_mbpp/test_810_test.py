import unittest
from mbpp_810_code import Counter
from your_module import count_variable  # replace 'your_module' with the actual module name where the function is defined

class TestCountVariable(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(count_variable([], [], [], []), [])

    def test_single_element(self):
        self.assertListEqual(count_variable([1], [], [], []), [1])
        self.assertListEqual(count_variable([], [1], [], []), [1])
        self.assertListEqual(count_variable([], [], [1], []), [1])
        self.assertListEqual(count_variable([], [], [], [1]), [1])

    def test_multiple_elements(self):
        self.assertListEqual(count_variable([1, 2, 2, 3], [4, 4, 5], [6, 6], [7, 7, 7]), [1, 2, 2, 3, 4, 4, 5, 6, 6])
