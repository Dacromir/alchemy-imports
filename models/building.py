from sqlalchemy import Column, Integer, String

if __name__ == "__main__":
    from base import Base
else:
    from .base import Base

class Building(Base):
    __tablename__ = "building"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    address = Column('address', String(50))

# Validate SQL output using SQLite in memory
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("sqlite:///:memory:", echo=True, future=True)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    test_building = Building(address="123 Test Street")

    session.commit()
    session.close()