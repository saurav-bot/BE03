from mysqlx import Session
from sqlalchemy import Column, Integer, String, create_engine, engine_from_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import env



Base = declarative_base()

class State(Base):
    __tablename__ = "states"

    id = Column('id', Integer, primary_key=True)
    state = Column("state", String(100))
    capital = Column("capital", String(100))


if __name__ == "__main__":

    engine = create_engine(f"mysql+mysqldb://{env.username}:{env.password}@localhost/test")

    Base.metadata.create_all(bind = engine)
    Session = sessionmaker(bind = engine)

    session = Session()

    entries = [("uttar pradesh", "lucknow"), ("karnataka", "bangalore"), ("maharashtra", "mumbai"), ("bihar", "patna"), ("pujab", "chandigarh"), ("rajasthan", "jaipur"), ('sikkim', "gangtok")]

    # i = 0
    for entry in entries:
        temp = State()
        # temp.id = i 
        temp.state = entry[0]
        temp.capital = entry[1]
        # i += 1

        session.add(temp)
    session.commit()

    session.close()




