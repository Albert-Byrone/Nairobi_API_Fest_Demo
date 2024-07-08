from sqlalchemy import String, Column, Text, Boolean, ForeignKey, Integer
from sqlalchemy.orm import relationship

from ..models import AbstractBaseModel


class Project(AbstractBaseModel):

    __tablename__ = 'projects'

    title = Column(String)
    image = Column(String)
    description = Column(Text)
    location =  Column(String)
    size =  Column(String)
    bedrooms=  Column(String)
    dsq =  Column(String)
    plot_size =  Column(String)
    prime_location =  Column(String)
    status =Column(String)
    experience = Column(String)




class Development(AbstractBaseModel):

    __tablename__ = 'developments'

    title = Column(String)
    image = Column(String)
    description = Column(Text)
    location =  Column(String)
    size =  Column(String)
    bedrooms=  Column(String)
    dsq =  Column(String)
    plot_size =  Column(String)
    prime_location =  Column(String)
    status =Column(String)
    experience = Column(String)



class Payment(AbstractBaseModel):
    __tablename__ ="payments"

    phone_number = Column(String)
    amount = Column(Integer)