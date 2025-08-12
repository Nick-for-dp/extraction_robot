import sys
sys.path.append('.')
import unittest

from manager import CustomerManager



class TestCustomerManager(unittest.TestCase):
    def setUp(self):
        self.customer_manager = CustomerManager()

    def test_get_all_customers(self):
        """测试get_all_customers方法,查看调用结果"""
        customers = self.customer_manager.get_all_customers()
        self.assertIsInstance(customers, list)
        print(customers)


if __name__ == '__main__':
    unittest.main()
