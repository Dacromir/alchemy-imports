from models.base import Base
from models.user import User
from models.building import Building

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///data.db", echo=True, future=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(username = "John Doe")
session.add(new_user)

new_building = Building(address = "123 Casanova St")
session.add(new_building)

session.commit()
session.close()