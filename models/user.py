from sqlalchemy import Column, Integer, String

if __name__ == "__main__":
    from base import Base
else:
    from .base import Base

class User(Base):
    __tablename__ = "user"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String(50))

# Validate SQL output using SQLite in memory
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("sqlite:///:memory:", echo=True, future=True)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    test_user = User(username="Test user")

    session.commit()
    session.close()