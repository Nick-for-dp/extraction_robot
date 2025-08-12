import json

from manager import CustomerManager
from robot.api import extract


def main():
    customer_manager = CustomerManager()
    user_input = r"""
    宏远建设集团有限公司来电咨询大宗钢铁采购事宜，该公司位于上海市浦东新区张江高科技园区博云路 2 号。负责人表示，因承接地铁 12 号线延伸段工程，需采购 1.2 万吨高强度螺纹钢（HRB400E）、8000 吨热轧卷板（Q235B），要求屈服强度≥335MPa，且每批次附材质证明书。
    对方特别强调，交货期需在 9 月 30 日前完成，分 3 批送达工地（地址：上海市松江区广富林路与茸惠路交叉口），首批 5000 吨需在 8 月 20 日前到岗。联系人：采购部李科长，电话 13901237890，邮箱 licang@hongyuangroup.com，希望本周内收到报价方案。
    """
    result = extract(user_input)
    extract_result = json.loads(result)
    print(type(extract_result), extract_result)
    customer_manager.create_customer_from_extract_result(extract_result)
    customers = customer_manager.get_all_customers()
    for customer in customers:
        print(customer)
    print("Hello from extraction-robot!")


if __name__ == "__main__":
    main()
