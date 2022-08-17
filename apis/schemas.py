from datetime import datetime
from pydantic import BaseModel

class Category(BaseModel):
    Name: str
    class Config():
        orm_mode=True


class user(BaseModel):
    Name: str
    email: str
    create_at: datetime
    class Config():
        orm_mode=True
        
class account(BaseModel):
    Name: str
    email: str
    create_at: datetime
    Intial_balance: str
    Account_type:str
    user_id:int
    class Config():
        orm_mode=True
        
class ledger(BaseModel):
    amount: int
    account_id: int
    category_id: int
    transaction: str
    transfer_to:str
    create_at: datetime
    user_id:int
    class Config():
        orm_mode=True
