from sqlalchemy import Column, String, ForeignKey
from app.db.base_class import Base

class RolePermission(Base):
    __tablename__ = "role_permissions"

    # Role ID Foreign Key (MySQL compatible String(36))
    role_id = Column(
        String(36), 
        ForeignKey("roles.id", ondelete="CASCADE"), 
        primary_key=True
    )
    
    # Permission ID Foreign Key (MySQL compatible String(36))
    permission_id = Column(
        String(36), 
        ForeignKey("permissions.id", ondelete="CASCADE"), 
        primary_key=True
    )

    def __repr__(self) -> str:
        return f"<RolePermission(role_id={self.role_id}, permission_id={self.permission_id})>"