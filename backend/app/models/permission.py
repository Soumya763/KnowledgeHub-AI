import uuid

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True,
    )

    name = Column(
        String(100),
        unique=True,
        index=True,
        nullable=False,
    )

    description = Column(
        String(255),
        nullable=True,
    )

    # Relationship with Roles (Many-to-Many)
    roles = relationship(
        "Role",
        secondary="role_permissions",
        back_populates="permissions",
    )

    def __repr__(self):
        return f"<Permission(name={self.name})>"