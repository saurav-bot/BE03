import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import env
from sqlalchemy.sql import text
from states import State


r = redis.Redis()

def fetch_data_from_db(key):
    engine = create_engine(f"mysql+mysqldb://{env.username}:{env.password}@localhost/test")
    Session = sessionmaker(bind=engine)
    session = Session()

    # capital = session.query(text("states")).filter(text("states.state") == key)
    result = session.query(State).all()
    # capital = session.query(State).filter(State.state == key)
    for res in result:
        if res.state == key:
            return res.capital
    
    return None

    return capital


while True:
    ans = input("enter a state to find it's capital: ")
    if ans == "exit":
        break

    if ans.lower() in  r:
        print("from cache")
        # print(r.get(ans.lower()))
        print(f"Capital of {ans} is {r.get(ans.lower()).decode()}")

    else:
        ans = ans.lower()
        cap = fetch_data_from_db(ans)

        
        if cap == None:
            print("Data Not available")
        else:
            r.set(ans, cap)
            print(f"Capital of {ans} is {cap}")


        # r.set(ans, cap)




