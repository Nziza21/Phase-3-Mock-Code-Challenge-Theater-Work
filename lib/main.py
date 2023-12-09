from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Audition, Role

# Connect to the database
engine = create_engine('sqlite:///theater.db')
Base.metadata.bind = engine

# Create a session to interact with the database
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Example usage
if __name__ == "__main__":
    # Create roles
    role1 = Role(character_name='Hero')
    role2 = Role(character_name='Villain')

    # Create auditions
    audition1 = Audition(actor='John Doe', location='Audition Room 1', phone=123456789, role=role1)
    audition2 = Audition(actor='Jane Doe', location='Audition Room 2', phone=987654321, role=role2)

    # Add roles and auditions to the session
    session.add_all([role1, role2, audition1, audition2])
    session.commit()

    # Query the database
    print("Roles:")
    for role in session.query(Role).all():
        print(f"Role: {role.character_name}")
        print(f"Auditions: {', '.join(audition.actor for audition in role.auditions)}")

    print("\nAuditions:")
    for audition in session.query(Audition).all():
        print(f"Actor: {audition.actor}, Role: {audition.role.character_name}, Hired: {audition.hired}")

    # Example: Call back an actor
    audition1.call_back()
    session.commit()

    print(f"\nAfter call back, Hired: {audition1.hired}")