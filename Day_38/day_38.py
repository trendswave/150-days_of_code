from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def main():
    # Check if the number of arguments is correct
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        return

    # Creating the connection string (engine for database)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Creating an instance of Session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Querying all State objects, sorted by id
        states = session.query(State).order_by(State.id).all()

        # Displaying the results
        for state in states:
            print("{:d}: {:s}".format(state.id, state.name))
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Closing the session
        session.close()


if __name__ == "__main__":
    main()
