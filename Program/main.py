
from database_manager import DatabaseManager

def main():
    # 1. load data from Database manager
    db_manager = DatabaseManager()
    db = db_manager.get_database()
    if not db:
        return

if __name__ == "__main__":
    main()