import unittest
from mbpp_669_code import check_IP

class TestCheckIP(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_IP('192.168.0.1'), "Valid IP address")

    def test_boundary_conditions(self):
        self.assertEqual(check_IP('255.255.255.255'), "Valid IP address")
        self.assertEqual(check_IP('0.0.0.0'), "Valid IP address")

    def test_edge_cases(self):
        self.assertEqual(check_IP('256.256.256.256'), "Invalid IP address")
        self.assertEqual(check_IP('192.168.0'), "Invalid IP address")
        self.assertEqual(check_IP('192.168.0.256'), "Invalid IP address")
        self.assertEqual(check_IP('192.168.0.-1'), "Invalid IP address")
        self.assertEqual(check_IP('abc.def.ghi.jkl'), "Invalid IP address")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_IP(19216801)
        with self.assertRaises(TypeError):
            check_IP([192, 168, 0, 1])
        with self.assertRaises(TypeError):
            check_IP({'ip': '192.168.0.1'})
