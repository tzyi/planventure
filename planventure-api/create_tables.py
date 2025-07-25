from sqlalchemy import create_engine
from models.user import Base
from models.trip import Trip  # 新增這行，確保 Trip 被註冊

# 這裡使用 SQLite，路徑與 .env 相同
engine = create_engine('sqlite:///./planventure.db')

def main():
    print("Creating all tables...")
    Base.metadata.create_all(bind=engine)
    print("All tables created.")

if __name__ == "__main__":
    main()
