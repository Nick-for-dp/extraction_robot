from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_name: str
    contact_info: Optional[str] = Field(default=None, description="The contact phone number of the customer")
    visit_time: datetime
    address: Optional[str] = Field(default=None, description="The address of the customer")
    new_demands: Optional[str] = Field(default=None, description="The new demands of the customer")
