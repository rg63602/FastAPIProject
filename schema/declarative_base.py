from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models"""

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()  # Table name will be the lowercase model name

    def as_dict(self):
        """Helper method to convert model instance to dictionary"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
