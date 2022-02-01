from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.sql.schema import Column
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    document = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime, default=datetime.now())
    
    #wallet = relationship("Wallet", back_populates="user")
    #user_payment = relationship("Payment", back_populates="user_payment")
