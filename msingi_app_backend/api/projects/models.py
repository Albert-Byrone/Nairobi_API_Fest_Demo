from sqlalchemy import String, Column, Text, Boolean, ForeignKey, Integer
from sqlalchemy.orm import relationship

from ..models import AbstractBaseModel


class Project(AbstractBaseModel):
    __tablename__ = 'projects'

    title = Column(String(32))
    description = Column(Text)
