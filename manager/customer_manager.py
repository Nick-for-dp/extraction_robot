from datetime import datetime
from typing import Dict, Any

from db.schema import Customer
from db.repo import CustomerRepository


class CustomerManager:
    def __init__(self):
        """
        初始化CustomerManager
        """
        self.customer_repo = CustomerRepository()
    
    def parse_extract_result(self, extract_result: Dict[str, Any]) -> Dict[str, Any]:
        """
        解析提取结果
        
        参数:
            extract_result: 从extract.py获取的提取结果
        
        返回:
            Dict[str, Any]: 解析后的客户信息字典
        """
        if not extract_result:
            return {}
        parsed_result = {
            'customer_name': extract_result.get('customer_name', ''),
            'contact_info': extract_result.get('contact_info', None),
            'visit_time': datetime.now(),
            'address': extract_result.get('address', None),
            'new_demands': extract_result.get('new_demands', None)
        }
        return parsed_result
    
    def create_customer_from_extract_result(self, extract_result: Dict[str, Any]) -> Customer | None:
        """
        从提取信息构建客户对象
        
        参数:
            extract_result: 用户文本信息提取结果
        
        返回:
            Customer: 创建的客户对象
        """
        
        # 解析提取结果
        parsed_result = self.parse_extract_result(extract_result)
        if not parsed_result:
            return None
        
        # 创建Customer对象
        customer = Customer(
            customer_name=parsed_result['customer_name'],
            contact_info=parsed_result['contact_info'],
            visit_time=parsed_result['visit_time'],
            address=parsed_result['address'],
            new_demands=parsed_result['new_demands']
        )
        
        # 保存到数据库
        return self.customer_repo.add_customer(customer)
    
    def get_all_customers(self) -> list[Customer]:
        """
        获取所有客户
        
        返回:
            list[Customer]: 所有客户的列表
        """
        return self.customer_repo.get_all_customers()
