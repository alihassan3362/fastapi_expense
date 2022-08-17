from apis.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("user", back_populates="user_1")
    
    creator_1 = relationship("ledger", back_populates="cate_1")


class user(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    create_at = Column(DateTime)
    user_1 = relationship("category", back_populates="creator")

    created_by = relationship("account", back_populates="client")
    
    creator_2 = relationship("ledger", back_populates="cate_2")

class account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    create_at = Column(DateTime)
    intial_balance = Column(String)
    Account_type = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    client = relationship("user", back_populates="created_by")
    
    creator_3 = relationship("ledger", back_populates="cate_3")


class ledger(Base):
    __tablename__ = 'ledger'
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(String)
    account_id = Column(String, ForeignKey("account.id"))
    category_id = Column(Integer, ForeignKey("category.id"))
    transaction = Column(String)
    transfer_to = Column(String)
    create_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))

    cate_1 = relationship("category", back_populates="creator_1")
    
    cate_2 = relationship("user", back_populates="creator_2")
    
    cate_3 = relationship("account", back_populates="creator_3")
