from app import app
from models import db

def main():
    print("Creating all tables...")
    with app.app_context():
        db.create_all()
    print("All tables created.")

if __name__ == "__main__":
    main()
