import uuid
from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Boolean, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = 'posts'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    category = Column(String, nullable=False)
    image = Column(String, nullable=False)
