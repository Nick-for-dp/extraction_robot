import sqlite3

from sqlmodel import create_engine


def init_database():
    """
    初始化SQLite数据库，创建dev.db文件和customer表
    """
    # 连接到数据库（如果不存在则创建）
    conn = sqlite3.connect('d:/projects/extraction_robot/db/dev.db')
    cursor = conn.cursor()
    
    # 创建customer表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name VARCHAR(50) NOT NULL,
        contact_info VARCHAR(50),
        visit_time DATETIME,
        address VARCHAR(100),
        new_demands VARCHAR(255)
    )
    ''')
    
    # 提交更改并关闭连接
    conn.commit()
    conn.close()
    
    print("数据库初始化成功，已创建dev.db和customer表")


def init_engine(database_name: str):
    sqlite_url = f"sqlite:///d:/projects/extraction_robot/db/{database_name}"
    engine = create_engine(sqlite_url)
    return engine

if __name__ == '__main__':
    # init_database()
    engine = init_engine("dev.db")
    print(type(engine))
