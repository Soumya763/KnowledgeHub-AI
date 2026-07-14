import uuid

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True,
    )

    name = Column(
        String(50),
        unique=True,
        index=True,
        nullable=False,
    )

    description = Column(
        String(255),
        nullable=True,
    )

    # Relationship with Users (Many-to-Many)
    users = relationship(
        "User",
        secondary="user_roles",
        back_populates="roles",
    )

    # Relationship with Permissions (Many-to-Many)
    permissions = relationship(
        "Permission",
        secondary="role_permissions",
        back_populates="roles",
    )

    def __repr__(self):
        return f"<Role(name={self.name})>"