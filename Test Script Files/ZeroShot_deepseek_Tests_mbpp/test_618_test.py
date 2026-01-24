import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):

    def test_div_list(self):
        self.assertEqual(div_list([1, 2, 3], [1, 2, 3]), [1, 1, 1])
        self.assertEqual(div_list([10, 20, 30], [1, 2, 3]), [10, 10, 10])
        self.assertEqual(div_list([1, 2, 3], [10, 20, 30]), [0.1, 0.1, 0.1])
        self.assertEqual(div_list([10, 20, 30], [10, 20, 30]), [1, 1, 1])
        self.assertEqual(div_list([], []), [])

        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            div_list([1, 2, 3], [0, 2, 3])

        # Test unequal length lists
        with self.assertRaises(ValueError):
            div_list([1, 2], [1, 2, 3])
