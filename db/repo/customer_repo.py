import sys
sys.path.append("..")

from sqlmodel import Session, select

from db.schema.customer import Customer
from db.init_db import init_engine


class CustomerRepository:
    def __init__(self, engine=None):
        """
        初始化CustomerRepository
        
        参数:
            engine: 数据库引擎，如果为None则使用默认引擎
        """
        self.engine = engine or init_engine("dev.db")
    
    def add_customer(self, customer: Customer) -> Customer:
        """
        添加一个新的客户到数据库
        
        参数:
            customer: 客户对象
        
        返回:
            Customer: 添加后的客户对象（包含id）
        """
        with Session(self.engine) as session:
            session.add(customer)
            session.commit()
            session.refresh(customer)
            return customer
    
    def get_all_customers(self) -> list[Customer]:
        """
        获取数据库中所有的客户
        
        返回:
            list[Customer]: 所有客户的列表
        """
        with Session(self.engine) as session:
            statement = select(Customer)
            results = session.exec(statement)
            return results.all()


if __name__ == "__main__":
    from datetime import datetime
    # 测试代码
    repo = CustomerRepository()
    
    # 示例: 添加一个客户
    test_customer = Customer(
        customer_name="测试客户",
        contact_info="13800138000",
        visit_time=datetime.now(),
        address="测试地址",
        new_demands="测试需求"
    )
    added_customer = repo.add_customer(test_customer)
    print(f"添加客户成功: {added_customer}")
    
    # 示例: 查询所有客户
    all_customers = repo.get_all_customers()
    print(f"所有客户: {all_customers}")
