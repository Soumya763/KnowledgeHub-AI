import uuid

from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        CHAR(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True,
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    username = Column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    hashed_password = Column(
        String(255),
        nullable=False,
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    # Relationship with Roles (Many-to-Many)
    roles = relationship(
        "Role",
        secondary="user_roles",
        back_populates="users",
    )

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"